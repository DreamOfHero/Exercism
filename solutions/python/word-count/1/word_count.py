"""Module to implement word frequency counter for subtitles."""
import string

# Valid characters for a word: lowercase letters and digits.
# Apostrophes are handled separately with context checks.
WORD_CHARS = string.ascii_lowercase + string.digits


def count_words(sentence):
    words = {}
    actual_word = ""

    # Normalize to lowercase so counting is case-insensitive.
    sentence_normalized = sentence.lower()

    for index, current_char in enumerate(sentence_normalized):
        is_allowed = is_char_allowed(current_char)

        # An apostrophe is valid only if both the preceding and following
        # characters are word characters (i.e. it's inside a contraction).
        # Leading/trailing apostrophes like 'word' are treated as separators.
        if current_char == "'":
            if index > 0 and index < len(sentence_normalized) - 1:
                previous_char = sentence_normalized[index - 1]
                next_char = sentence_normalized[index + 1]
                is_allowed = is_char_allowed(previous_char) and is_char_allowed(next_char)

        if is_allowed:
            actual_word += current_char
        else:
            # Current character is a separator: flush the accumulated word.
            update_word_count(actual_word, words)
            actual_word = ""

    # Flush the last word in case the sentence doesn't end with a separator.
    update_word_count(actual_word, words)
    return words


def is_char_allowed(char):
    # Returns True if the character is a valid word character.
    return char in WORD_CHARS


def update_word_count(word, words):
    # Increments the word count, ignoring empty strings.
    if word:
        words[word] = words.get(word, 0) + 1