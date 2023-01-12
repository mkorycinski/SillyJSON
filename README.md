# SillyJSON
A rather silly implementation of a JSON parser using Python with some help from regular expressions.

## Install
Use pip with available eggs, e.g.:
```bash
pip install ./silly-json.egg
```

## Usage
```python
from silly_json import load, loads

# Parse a file
data = load('/path/to/a/file')

# Parse a string
data = loads('{"foo": "bar"}')
```

## Disclaimer
This code was written as a final project in the "Automate the Boring Stuff" course provided by the Doctoral School of Information and Biomedical Technologies at the Polish Academy of Sciences - [TIB PAN](https://tib.ippt.pan.pl/). 