import unittest
from unittest_expander import expand, foreach

from silly_json.value_parsers import ValueParser
from silly_json.errors import NotExpectedType


@expand
class TestValueParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = ValueParser()

    @foreach(
        ('123', 123),
        ('1', 1),
        ('true', True),
        ('false', False),
        ('123.22', 123.22),
        ('1.22', 1.22),
        ('1e-3', 0.001),
        ('null', None),
        ('"Jan Kowalski"', 'Jan Kowalski'),
        ('"Abecadlo"', 'Abecadlo'),
        ('"1null"', '1null'),
        ('"null1"', 'null1'),
        ('"1.23aslkdl"', '1.23aslkdl'),
        ('"kjk1.23"', 'kjk1.23'),
        ('"kjk1.23kjk"', 'kjk1.23kjk')
    )
    def test_values(self, test_str, expected):
        self.assertEqual(self.parser(test_str), expected)
