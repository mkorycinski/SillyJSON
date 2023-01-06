import unittest
from unittest_expander import expand, foreach

from silly_json.value_parsers import IntegerParser
from silly_json.errors import NotExpectedType

@expand
class TestIntegerParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = IntegerParser()

    @foreach(
        ('123', 123),
        ('1', 1),
    )
    def test_integers(self, test_str, expected):
        self.assertEqual(self.parser(test_str), expected)


    @foreach(
        '1aslkdl', 'kjk1', 'kjk1kjk'
    )
    def test_wrong_str(self, test_str):
        with self.assertRaises(NotExpectedType):
            self.parser(test_str)
