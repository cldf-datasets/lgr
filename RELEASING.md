# The Leipzig Glossing Rules as CLDF dataset

This CLDF dataset contains the examples used in the specification of the Leipzig Glossing Rules (LGR)
in a CLDF ExampleTable, as well as the specification itself as CLDF Markdown document.
This CLDF data is used to render the LGR document in Markdown in [README.md](README.md).

The idea of this dataset is
- to provide the rules in an editable, more accessible format
- to create an archival package of the rules suitable for depositing on Zenodo
- to provide the examples in a machine readable format suitable for usage as a test suite for
  software that deals with interlinear glossed text.


## Releasing LGR

The CLDF data is curated "in situ", i.e. **not** recreated from a different source via `makecldf`.
Thus, releasing LGR means making sure the data is valid and then creating the derived metadata.

Install `cldfviz`.

Make sure the CLDF dataset is valid:
```shell
cldf validate cldf
```

Check the metadata:
```shell
cldf stats cldf
```

Create metadata for Zenodo:
```shell
cldfbench zenodo cldfbench_lgr.py
cldfbench cldfreadme cldfbench_lgr.py
```

Render the full document describing the rules by running
```shell
cldfbench cldfviz.text --media-id lgr --output README.md --templates templates cldf
```
