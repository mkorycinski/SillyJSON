from .json_parser import JSONParser


def load(fpath: str) -> object:
    parser = JSONParser()
    with open(fpath, 'r') as jfile:
        return parser(jfile.read())


def loads(x: str) -> object:
    parser = JSONParser()
    return parser(x)
