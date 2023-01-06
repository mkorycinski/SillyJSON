import re

from silly_json.errors import NotExpectedType


class GenericParser:
    pattern = ''
    caster = str

    def __init__(self):
        self.pattern = re.compile(self.pattern)

    def __call__(self, input_str: str):
        match = re.match(self.pattern, input_str)
        if match:
            return self.caster(match.group())
        else:
            raise NotExpectedType


class IntegerParser(GenericParser):
    pattern = r'^[1-9][0-9]*$'
    caster = int


class FloatParser(GenericParser):
    exponent = r'[eE][-+]?[0-9]+'
    num_pattern = '[0-9]*'
    pattern = fr'^({num_pattern}.{num_pattern}({exponent})?)$|^({num_pattern}{exponent})$'
    caster = float


class StringParser(GenericParser):
    pattern = r'^.+$'


class BoolParser(GenericParser):
    def __call__(self, input_str):
        if input_str == 'true':
            return True
        elif input_str == 'false':
            return False
        else:
            raise NotExpectedType


class NullParser(GenericParser):
    def __call__(self, input_str):
        if input_str == 'null':
            return None
        else:
            raise NotExpectedType


class ValueParser:
    def __init__(self):
        self.parsers = [
            IntegerParser(),
            FloatParser(),
            BoolParser(),
            NullParser(),
            StringParser()
        ]

    def __call__(self, input_str: str):
        for par in self.parsers:
            try:
                return par(input_str)
            except NotExpectedType:
                pass
        raise NotExpectedType
