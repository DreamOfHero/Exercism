"""Module to implement NANP phone number cleaning and validation."""
import string
# Set of characters that are allowed in raw input before digit extraction.
# Anything outside this set that is not a letter triggers "punctuations not permitted".
VALID_CHARS = set(string.digits + "()+-. ")

def clean(number):
    # Validate characters first, before stripping anything,
    # so error messages reflect the original input.
    validate_characters(number)
    # Strip everything except digits — spaces, dashes, dots, parentheses.
    number = "".join(char for char in number if char.isdigit())
    validate_length(number)
    # If 11 digits, the leading digit must be the country code 1 — then strip it.
    if len(number) == 11:
        if number[0] != "1":
            raise ValueError("11 digits must start with 1")
        number = number[1:]
    validate_codes(number)
    return number

def validate_characters(number):
    # Letters and invalid punctuation are checked separately
    # because they produce different error messages.
    for char in number:
        if char.isalpha():
            raise ValueError("letters not permitted")
        if char not in VALID_CHARS:
            raise ValueError("punctuations not permitted")

def validate_length(number):
    # Length is checked after stripping formatting, on digits only.
    if len(number) < 10:
        raise ValueError("must not be fewer than 10 digits")
    if len(number) > 11:
        raise ValueError("must not be greater than 11 digits")

def validate_codes(number):
    # After stripping the country code, the number is always 10 digits.
    # Area code is digits 0-2, exchange code is digits 3-5.
    area_code = number[:3]
    exchange_code = number[3:6]
    if area_code[0] == "0":
        raise ValueError("area code cannot start with zero")
    if area_code[0] == "1":
        raise ValueError("area code cannot start with one")
    if exchange_code[0] == "0":
        raise ValueError("exchange code cannot start with zero")
    if exchange_code[0] == "1":
        raise ValueError("exchange code cannot start with one")

class PhoneNumber:
    def __init__(self, number):
        # All cleaning and validation happens in clean().
        # If the number is invalid, a ValueError is raised before assignment.
        self._number = clean(number)
        self._area_code = self._number[:3]
        self._exchange_code = self._number[3:6]

    @property
    def number(self):
        return self._number

    @property
    def area_code(self):
        return self._area_code

    @property
    def exchange_code(self):
        # Exposed as a property for completeness, even though not required by tests.
        return self._exchange_code

    def pretty(self):
        # Format: (NXX)-NXX-XXXX
        return f"({self.area_code})-{self.exchange_code}-{self.number[6:]}"