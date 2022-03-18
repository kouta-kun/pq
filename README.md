# pq

PQ is a jq-like viewer/processing tool for pickle files.

# howto

```bash
# pq '' file.pkl
{'other': 456, 'test': 123}
# pq '' file.pkl -f table
|other|test|
| 456 |123 |
# pq 'keys' file.pkl
['test', 'other']
# pq '.["test"]' file.pkl
123
# pq 'eval({"value": i["other"] + i["test"]})' file.pkl -f table
|value|
|=====|
| 579 |
```

# Implemented filters

| Filter | Usage | Description |
| ------ | ----- | ----------- |
| flat   | `.[]`    | Extract elements from list to apply filters on each |
| keys   | `keys`  | Extract keys from dictionary or list(range(len(list))) on a list |
| accessor | `.ATTRIBUTE` or `.[INDEX]` | Read attribute from object or index on a list/dictionary |
| sort | `sort(FILTEREXPR)` | Order elements by result of filter expression (accessor, eval) |
| eval | `eval(EVALEXPR)` | Apply EVALEXPR on items of list. EVALEXPR is a python expression with i as parameter (example: i["separation"], {"firstname": i["name"].split()[0], "lastname": i["name"].split()[1]}) |

# Formatting filters

| Type | Description |
| ---- | ----------- |
| pretty | DEFAULT, pretty prints python structure (pprint module) |
| table | prints list of dictionaries as a table (only common keys) |