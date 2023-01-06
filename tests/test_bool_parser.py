import unittest
from unittest_expander import expand, foreach

from silly_json.value_parsers import BoolParser
from silly_json.value_parsers import NotExpectedType


@expand
class TestBoolParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = BoolParser()

    @foreach(
        ('true', True),
        ('false', False)
    )
    def test_proper(self, test_str, expected):
        self.assertEqual(self.parser(test_str), expected)

    @foreach(
        'yes true', 'true something',
        'no false', 'false no',
        '111false', 'false111',
        'True', 'False'
    )
    def test_improper(self, test_str):
        with self.assertRaises(NotExpectedType):
            self.parser(test_str)
