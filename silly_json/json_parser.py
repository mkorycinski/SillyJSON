import re
from typing import Any

from silly_json.value_parsers import ValueParser
from silly_json.utils import object_splitter, split_string_on_first


class JSONParser:

    def __init__(self):
        """
        Main class for parsing a JSON-formatted string.
        """
        self.array_pattern = re.compile(r'^\[.*\]$')
        self.object_pattern = re.compile(r'^\{.*\}$')
        self.value_parser = ValueParser()

    def __call__(self, input_str: str) -> Any:
        """
        Parses input string recursively. If an array
        or object is detected it will be called again
        with the content of that object. That way
        it is an easy way to parse embedded JSON
        structures.

        Args:
            input_str: JSON-formatted string

        Returns:
            A valid python object parsed from JSON.
        """
        input_str = input_str.replace('\t', '').replace('\n', '').strip()
        if re.match(self.array_pattern, input_str):
            return [
                self(value.strip())
                for value
                in object_splitter(input_str=input_str)
            ]

        elif re.match(self.object_pattern, input_str):
            return {
                k.strip().replace('"', ''): self(v.strip())
                for k, v
                in [
                    split_string_on_first(elem, ':')
                    for elem
                    in object_splitter(input_str=input_str)
                ]
            }
        else:
            return self.value_parser(input_str)
