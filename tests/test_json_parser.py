import json
import unittest

from unittest_expander import expand, foreach

from silly_json import JSONParser


JSON1 = '[1, 0.001, true, false, null, "ja,cek"]'
JSON2 = '{"foo": "bar", "ilosc": 1, "waga": 0.001, "lubie": false}'
JSON3 = '{"name": "Artur", "wife": null, "children": ["Małgorzata", "Bartek"], ' \
        '"criminal history": true, "weight": 73.5, "fridge content": {"egg": 4, "ham": "200g"}}'
JSON4 = """
{
    "name": "Artur",
    "wife": null,
    "children": ["Małgorzata", "Bartek"],
    "criminal history": true,
    "weight": 73.5,
    "fridge content": {
        "egg": 4,
        "ham": "200g"
    }
}
"""


@expand
class TestJsonParser(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = JSONParser()

    @foreach(JSON2, JSON3, JSON4)
    def test_json_parser_on_strings_with_objects(self, input_str):
        expected = json.loads(input_str)
        parsed = self.parser(input_str=input_str)
        self.assertDictEqual(expected, parsed)

    @foreach(
        '["J,acek", "Natalia"]', '[1,2,3,4,5]', JSON1
    )
    def test_json_parser_on_string_with_arrays(self, input_str):
        expected = json.loads(input_str)
        parsed = self.parser(input_str)
        self.assertListEqual(expected, parsed)



