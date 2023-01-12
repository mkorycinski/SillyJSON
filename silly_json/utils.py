import re
from typing import List

_OBJECT_BOUNDARY_MAPPING = {
    '"': '"',
    '{': '}',
    '[': ']'
}


def split_string_on_first(s: str, split_char: str) -> List[str]:
    """
    Splits given string into two based on the first
    occurrence of the split_character. If a given character
    does not occur, a list contains a single string.

    Args:
        s: A string to split
        split_char: A character to split with

    Returns:
        A list of strings after the split.
    """
    split_char_pos = s.find(split_char)
    if split_char_pos == -1:
        return [s, ]
    return [s[:split_char_pos], s[split_char_pos + 1:]]


def rejoin_element(arr: list, object_end: str) -> (int, str):
    """
    Iterates over an array `arr` to reach
    an element ending with an `object_end`
    character. If reached all elements
    are joined together with a comma.

    Args:
        arr: Array to iterate over
        object_end: Character with which
                    an object shall end

    Returns:
        Position of the last element and
        a string joined from elements by
        a comma.
    """
    record = []

    # start iterating from element onwards
    # to reach element having closing char
    for j, ne in enumerate(arr):
        record.append(ne)
        # break when we reach it
        if ne[-1] == object_end:
            break
    return j, ','.join(record)


def object_splitter(input_str: str) -> list[str]:
    """
    Allows to split correctly arrays and objects
    nested in the JSON string.

    Args:
        input_str: JSON string

    Returns:
        A list of object elements as strings
    """
    output = []

    # Greedy split on each comma
    inp = [e.strip() for e in input_str[1:-1].strip().split(',')]
    # since we have to offset some elements a for loop
    # cannot do this for us and we have to manually manage i var
    i = 0
    while i < len(inp):
        elem = inp[i]

        # Check whether an element represents one of these:
        # string -> "
        # array -> [
        # object -> {
        object_begin_match = re.match(r'^[\{\["]', elem)

        # if it does not -> just add to the output
        if not object_begin_match:
            output.append(elem)
            i += 1
        else:
            # what kind of object do we see? -> ", [, {
            object_begin = object_begin_match.group()
            # get the closing character -> ", }, ]
            object_end = _OBJECT_BOUNDARY_MAPPING[object_begin]

            # check if we deal with the object k:v pair
            # if so, then the closing object end will
            # be after the colon
            if re.match(r'^".*?"\s*:\s*.*$', elem):
                value_first_char = re.match(r'^".*?"\s*:\s*.', elem).group()[-1]
                # check whether the value is an object, if yes set the closing
                # char so it can be rejoined
                if value_first_char in _OBJECT_BOUNDARY_MAPPING.keys():
                    j, rejoined = rejoin_element(
                        inp[i:], object_end=_OBJECT_BOUNDARY_MAPPING[value_first_char]
                    )
                    output.append(rejoined)
                    i += j + 1
                else:
                    # if it is not an object but e.g. string,
                    # just add it and move on
                    output.append(elem)
                    i += 1
                continue

            # see if the element is not closed within itself
            # e.g. object with one k:v pair, string without comma inside
            elif re.match(f'^{object_begin}.*{object_end}$', elem):
                output.append(elem)
                i += 1
                continue
            else:
                j, rejoined = rejoin_element(arr=inp[i:], object_end=object_end)
                # rejoin object / string
                output.append(rejoined)
                # rewind i index to the next element after
                # the one having closing char
                i += j + 1
    return output
