import string

# Alphabet used for rotation (lowercase letters only)
ALPHABET = string.ascii_lowercase

# Mapping each character to its index for fast lookup
CHAR_TO_INDEX = {char: i for i, char in enumerate(ALPHABET)}


def rotate(text, key):
    """Apply a rotational cipher to the given text using the provided key."""
    converted_chars = []

    # Process each character in the input text
    for char in text:
        if char.isalpha():
            # Rotate alphabetic characters
            converted_chars.append(convert_char(char, key))
        else:
            # Preserve non-alphabetic characters
            converted_chars.append(char)

    # Join all converted characters into the final string
    return "".join(converted_chars)


def convert_char(char, key):
    """Rotate a single alphabetic character, preserving its case."""
    # Compute the new index using modular arithmetic
    index_char = (CHAR_TO_INDEX[char.lower()] + key) % len(ALPHABET)

    # Get the rotated character
    new_char = ALPHABET[index_char]

    # Restore uppercase if needed
    if char.isupper():
        new_char = new_char.upper()

    return new_char
