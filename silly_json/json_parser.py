from .parsers.array_parser import ArrayParser
from .parsers.bool_parser import BoolParser
from .parsers.float_parser import FloatParser
from .parsers.integer_parser import IntegerParser
from .parsers.null_parser import NullParser
from .parsers.object_parser import ObjectParser
from .parsers.string_parser import StringParser


class JSONParser:
    PARSERS = {
        ArrayParser.PATTERN: ArrayParser,
        BoolParser.PATTERN: BoolParser,
        FloatParser.PATTERN: FloatParser,
        IntegerParser.PATTERN: IntegerParser,
        NullParser.PATTERN: NullParser,
        ObjectParser.PATTERN: ObjectParser,
        StringParser.PATTERN: StringParser
    }

    def __call__(self, x):
        return {'foo': 'bar'}