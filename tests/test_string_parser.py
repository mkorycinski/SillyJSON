import unittest
from unittest_expander import expand, foreach

from silly_json.value_parsers import StringParser


@expand
class TestStringParser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = StringParser()

    @foreach(
        ('Jan Kowalski', 'Jan Kowalski'),
        ('Abecadlo', 'Abecadlo')
    )
    def test_proper(self, test_str, expected):
        self.assertEqual(self.parser(test_str), expected)
