import unittest

from unittest_expander import expand, foreach

from silly_json.utils import object_splitter

@expand
class TestObjectSplitter(unittest.TestCase):

    @foreach(
        (
            '[1, 0.001, true, false, null, "ja,cek", "jacek"]',
            ['1', '0.001', 'true', 'false', 'null', '"ja,cek"', '"jacek"']
        ),
        (
            '[1, 0.001, true, false, null, "ja,cek", "jacek", {"foo: "bar"}, {"foo: "bar", ' \
            '"foo: "b,ar"}]',
            ['1', '0.001', 'true', 'false', 'null', '"ja,cek"', '"jacek"', '{"foo: "bar"}',
             '{"foo: "bar","foo: "b,ar"}']
        ),
        (
            '{"foo: "bar", "foo: "b,ar"}',
            ['"foo: "bar"', '"foo: "b,ar"']
        ),
        (
            '{"foo": "bar", "ilosc": 1, "waga": 0.001, "lubie": false}',
            ['"foo": "bar"', '"ilosc": 1', '"waga": 0.001', '"lubie": false']
        )
    )
    def test_object_splitter(self, input_str, expected):
        self.assertListEqual(object_splitter(input_str=input_str), expected)