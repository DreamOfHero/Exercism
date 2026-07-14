"""Module to implement Scrabble word score calculator."""

# Dictionary mapping each uppercase letter to its Scrabble point value.
SCRABBLE_VALUES = {
    "A": 1, "B": 3, "C": 3, "D": 2,
    "E": 1, "F": 4, "G": 2, "H": 4,
    "I": 1, "J": 8, "K": 5, "L": 1,
    "M": 3, "N": 1, "O": 1, "P": 3,
    "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 4, "X": 8,
    "Y": 4, "Z": 10
}


def char_value(char):
    # Single point of access to the score data structure.
    # If the data source changes, only this function needs to be updated.
    return SCRABBLE_VALUES[char]


def score(word):
    # Normalize to uppercase to match the keys in SCRABBLE_VALUES.
    upper_word = word.upper()
    word_score = 0
    for current_char in upper_word:
        word_score += char_value(current_char)
    return word_score
