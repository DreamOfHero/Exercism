"""Module to implement the Luhn algorithm for number validation."""


class Luhn:
    def __init__(self, card_num):
        # Strip spaces immediately so all subsequent logic works on digits only.
        self.card_number = card_num.replace(" ", "")

    def valid(self):
        sum_digits = 0
        # Tracks how many doubled values exceeded 9.
        # Instead of subtracting 9 inline, we collect the count and
        # apply the correction in a single operation at the end.
        subtract_nine_count = 0

        # A number with 1 or fewer digits is always invalid,
        # as is any string containing non-digit characters.
        if len(self.card_number) <= 1 or not self.card_number.isdigit():
            return False

        # Iterate over the digits in reverse order.
        # Every second digit (index 1, 3, 5, ...) gets doubled.
        for index, digit in enumerate(self.card_number[::-1]):
            value = int(digit)
            if index % 2 != 0:
                value *= 2
                if value > 9:
                    subtract_nine_count += 1
            sum_digits += value

        # Apply the Luhn correction: each doubled value that exceeded 9
        # is equivalent to subtracting 9 from the total.
        sum_digits -= (9 * subtract_nine_count)

        return sum_digits % 10 == 0