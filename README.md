# foto-teodolito-graph

For displaying the results measured with [this instrument](https://github.com/lopezsolerluis/foto-teodolito) and [code](https://github.com/lopezsolerluis/foto-teodolito-log).

## Usage

```python
python graph.py <name_of_csv_file> [log]
```

If `log` is given, the values measured are passed to `numpy.log10()` first, turning the graph into a logarithmic graph.

## Folders

* `data`: Where the *csv* files ares stored in this repo.
* `graphs`: Where the graphs are stored in this repo.
