# pq

PQ is a jq-like viewer/processing tool for pickle files.

# howto

```bash
# pq '' file.pkl
{'other': 456, 'test': 123}
# pq 'table' file.pkl
|other|test|
| 456 |123 |
# pq 'keys' file.pkl
['test', 'other']
# pq '.["test"]' file.pkl
123
```

# Implemented filters

| Filter | Usage | Description |
| ------ | ----- | ----------- |
| flat   | .[]    | Extract elements from list to apply filters on each |
| table  | table | When elements are dictionaries, display common keys as a table |
| keys   | keys  | Extract keys from dictionary or list(range(len(list))) on a list |
| accessor | .ATTRIBUTE or .[INDEX] | Read attribute from object or index on a list/dictionary |
