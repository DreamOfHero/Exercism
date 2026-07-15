"""Module to implement the Proverb rhyme generator."""


def proverb(*items, qualifier):
    phrases = []

    # Build one "For want of..." line for each consecutive pair of items.
    # zip stops automatically when the shorter iterable is exhausted,
    # so the last item is never used as a "first" element here.
    for first, second in zip(items[:-1], items[1:]):
        phrases.append(f"For want of a {first} the {second} was lost.")

    # Append the closing line only if there are items to work with.
    last_phrase = create_last(items, qualifier)
    if last_phrase:
        phrases.append(last_phrase)

    return phrases


def create_last(items, qualifier):
    # Empty input produces no closing line.
    if not items:
        return ""

    # If qualifier is None or empty, fall back to an empty string
    # to avoid the word "None" appearing in the output.
    qualifier_prefix = qualifier or ""

    # Combine qualifier and first item, then strip any leading/trailing
    # whitespace that would appear when qualifier_prefix is empty.
    to_replace = f"{qualifier_prefix} {items[0]}"
    return f"And all for the want of a {to_replace.strip()}."