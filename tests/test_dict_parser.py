import unittest
from unittest_expander import expand, foreach

from silly_json.object_parsers import DictParser



@expand
class TestArrayParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = DictParser()

    @foreach(
        ('[1,2,3,4]', False),
        ('["foo", "bar"]', False),
        ('{"foo": "bar", "foo2": 2}', True),
        ('foobar', False),
        ('1234', False)
    )
    def test_array_parser(self, test_str, expected):
        self.assertEqual(self.parser.is_of_type(test_str), expected)
