"""

"""
import re
import urllib.parse

from pycldf import orm
import jinja2

from cldfbench_lgr import Dataset

MD_LINK_PATTERN = re.compile(r'\[(?P<label>[^]]+)]\((?P<url>[^)]+)\)')


def render_template(d, fname_or_component, obj, index=False, fmt='md'):
    templateLoader = jinja2.FileSystemLoader(searchpath=str(d))
    templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True)
    template = templateEnv.get_template('{}_{}.{}'.format(
        fname_or_component, 'index' if index else 'detail', fmt))
    return template.render(ctx=obj)


def run(args):
    ds = Dataset()
    cldf = ds.cldf_reader()

    datadict, table_map = {}, {}
    for table in cldf.tables:
        fname = str(table.url)
        if (fname, 'id') in cldf:
            try:
                table_map[fname] = cldf.get_tabletype(table)
            except ValueError:
                table_map[fname] = None
            objs = cldf.objects(table_map[fname]) if table_map[fname] else cldf.iter_rows(fname, 'id')
            datadict[fname] = {r.id if isinstance(r, orm.Object) else r['id']: r for r in objs}
    datadict[cldf.bibname] = {src.id: src for src in cldf.sources}
    table_map[cldf.bibname] = 'Source'

    print(''.join(iter_md(ds, datadict, table_map)))


def iter_md(ds, datadict, table_map):
    md = ds.dir.joinpath('README_tmpl.md').read_text(encoding='utf8')
    current = 0
    for m in MD_LINK_PATTERN.finditer(md):
        yield md[current:m.start()]
        current = m.end()
        url = urllib.parse.urlparse(m.group('url'))
        fname = url.path.split('/')[-1]
        if url.fragment.startswith('cldf:') and fname in datadict:
            type_ = table_map[fname]
            _, _, oid = url.fragment.partition(':')
            if oid == '__all__':  # look up the "index" template
                yield render_template(
                    ds.dir / 'templates', type_ or fname, datadict[fname].values(), index=True)
            else:  # look up "detail" template
                yield render_template(
                    ds.dir / 'templates', type_ or fname, datadict[fname][oid])
    yield md[current:]
