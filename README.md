# rconfig

A config loader and parser for Python.

## Support File Type

- `.yaml`

## Example

```python
from rconfig import config
config = Config.from_file('./data/example.yaml)
print(config.TEST.DATA)
```
