"""

"""
import re
import urllib.parse

from pycldf import orm
from jinja2 import Template

from cldfbench_lgr import Dataset

MD_LINK_PATTERN = re.compile(r'\[(?P<label>[^]]+)]\((?P<url>[^)]+)\)')

def render_example(e):
    print(e.cldf)
    template = Template("""
<blockquote>
({{ example.id }}) {{ example.related('languageReference').name }}{% if example.references %}
 ([{{ example.references[0].source.id }}](#source-{{ example.references[0].source.id }}){% if example.references[0].description %}
: {{ example.references[0].description }}{% endif %}){% endif %}


{% for word in example.cldf.analyzedWord %}{% if loop.first != True %} | {% endif%}{{ word }}{% endfor %}

{% for word in example.cldf.analyzedWord %}{% if not loop.first %}|{% endif%} --- {% endfor %}

{% for word in example.cldf.gloss %}{% if not loop.first %} | {% endif%}{{ word }}{% endfor %}


‘{{ example.cldf.translatedText }}’
</blockquote>
""", trim_blocks=True)
    return template.render(example=e)


def run(args):
    ds = Dataset()
    cldf = ds.cldf_reader()

    datadict, table_map = {}, {}
    for table in cldf.tables:
        fname = str(table.url)
        if (fname, 'id') in cldf:
            table_map[fname] = cldf.get_tabletype(table)
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
            if type_ == 'ExampleTable':
                yield render_example(datadict[fname][oid])
            elif type_ == 'Source':
                yield datadict[fname][oid].text()
    yield md[current:]
