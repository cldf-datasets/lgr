# Releasing LGR

Install `cldfviz`.

Make sure the CLDF dataset is valid:
```shell
cldf validate cldf
```

Check the metadata:
```shell
cldf stats cldf
```

Render the full document describing the rules by running
```shell
cldfbench cldfviz.text --media-id lgr --output README.md --templates templates cldf
```
