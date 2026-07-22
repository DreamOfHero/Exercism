"""Module to implement text transposition."""


def transpose(text):
    lines = text.split("\n")

    # Find the length of the longest row — this determines how many
    # output rows the transposed result will have.
    max_len = max(len(line) for line in lines)

    result = []
    for column in range(max_len):
        new_line = ""
        for row, line in enumerate(lines):
            if column < len(line):
                # The current row has a character at this column: use it.
                new_line += line[column]
            else:
                # The current row is shorter than the column index.
                # Add a space only if a later row still has a character
                # at this column — otherwise we'd be padding to the right,
                # which the rules forbid.
                if has_char_below(lines, row, column):
                    new_line += " "
        result.append(new_line)

    return "\n".join(result)


def has_char_below(lines, row, column):
    # Check whether any row below the current one has a character
    # at the given column index.
    for next_row in range(row + 1, len(lines)):
        if len(lines[next_row]) > column:
            return True
    return False