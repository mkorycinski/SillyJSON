import unittest
from unittest_expander import expand, foreach

from silly_json.value_parsers import NullParser
from silly_json.value_parsers import NotExpectedType


@expand
class TestBoolParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = NullParser()

    def test_proper(self):
        self.assertEqual(self.parser('null'), None)

    @foreach('Null', 'nulle', '1null', 'null1')
    def test_improper(self, test_str):
        with self.assertRaises(NotExpectedType):
            self.parser(test_str)
