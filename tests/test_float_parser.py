import unittest
from unittest_expander import expand, foreach

from silly_json.value_parsers import FloatParser
from silly_json.errors import NotExpectedType


@expand
class TestFloatParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = FloatParser()

    @foreach(
        ('123.22', 123.22),
        ('1.22', 1.22),
        ('1e-3', 0.001),
        ('0.001', 0.001),
        ('-0.001', -0.001),
        ('-1e-3', -0.001)
    )
    def test_proper(self, test_str, expected):
        self.assertEqual(self.parser(test_str), expected)

    @foreach('1.23aslkdl', 'kjk1.23', 'kjk1.23kjk')
    def test_improper(self, test_str):
        with self.assertRaises(NotExpectedType):
            self.parser(test_str)
