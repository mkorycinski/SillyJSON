import re

from silly_json.errors import NotExpectedType


class GenericParser:
    pattern = ''
    caster = str

    def __init__(self):
        self.pattern = re.compile(fr'^{self.pattern}$')

    def __call__(self, input_str: str):
        match = re.match(self.pattern, input_str)
        if match:
            return self.caster(match.group())
        else:
            raise NotExpectedType


class IntegerParser(GenericParser):
    pattern = r'0|-{0,1}[1-9][0-9]*'
    caster = int


class FloatParser(GenericParser):
    exponent = r'[eE][-+]?[0-9]+'
    num_pattern = '-{0,1}[0-9]*'
    pattern = fr'({num_pattern}.{num_pattern}({exponent})?)$|^({num_pattern}{exponent})'
    caster = float


class StringParser(GenericParser):
    pattern = r'".+"'

    def __call__(self, input_str: str):
        result = super().__call__(input_str=input_str)
        return result[1:-1]


class BoolParser(GenericParser):
    pattern = 'true|false'
    mapping = {
        'true': True,
        'false': False
    }

    def __init__(self):
        self.pattern = re.compile('^true$|^false$')

    def __call__(self, input_str):
        result = super().__call__(input_str=input_str)
        return self.mapping[result]


class NullParser(GenericParser):
    pattern = 'null'

    def __call__(self, input_str):
        super().__call__(input_str=input_str)
        return None


class ValueParser:
    parsers = [
        FloatParser,
        IntegerParser,
        BoolParser,
        NullParser,
        StringParser
    ]
    pattern = '|'.join(
        [
            p.pattern
            for p in parsers
        ]
    )

    def __init__(self):
        self.parsers = [
            parser()
            for parser in self.parsers
        ]

    def __call__(self, input_str: str):
        for par in self.parsers:
            try:
                return par(input_str)
            except NotExpectedType:
                pass
        raise NotExpectedType
