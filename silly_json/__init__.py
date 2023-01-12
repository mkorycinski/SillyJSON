from .json_parser import JSONParser


def load(fpath: str) -> object:
    """
    Parse a JSON file.
    Args:
        fpath: A path to a JSON file.

    Returns:
        Parsed json as an object.
    """
    parser = JSONParser()
    with open(fpath, 'r') as jfile:
        return parser(jfile.read())


def loads(s: str) -> object:
    """
    Parses a JSON-formatted string.
    Args:
        s: JSON-formatted string.

    Returns:
        Parsed json as an object.
    """
    parser = JSONParser()
    return parser(s)
