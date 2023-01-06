import re

from silly_json.errors import NotExpectedType


class ObjectParser:
    pattern = ''

    def is_of_type(self, input_str):
        return bool(re.match(self.pattern, input_str))


class ArrayParser(ObjectParser):
    pattern = '^\[.*\]$'

    def __call__(self, input_str: str) -> []:
        return []


class DictParser(ObjectParser):
    pattern = '^\{.*\}$'

    def __call__(self, input_str: str) -> {}:
        return {}
