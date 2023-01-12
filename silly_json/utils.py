import re

_OBJECT_BOUNDARY_MAPPING = {
    '"': '"',
    '{': '}',
    '[': ']'
}


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
    inp = [e.strip() for e in input_str[1:-1].split(',')]

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

            # see if the element is not closed within itself
            # e.g. object with one k:v pair, string without comma inside
            if re.match(f'^{object_begin}.*{object_end}$', elem):
                output.append(elem)
                i += 1
                continue
            else:
                record = []

                # start iterating from element onwards
                # to reach element having closing char
                for j, ne in enumerate(inp[i:]):
                    record.append(ne)
                    # break when we reach it
                    if ne[-1] == object_end:
                        break
                # rejoin object / string
                output.append(','.join(record))
                # rewind i index to the next element after
                # the one having closing char
                i += j + 1
    return output
