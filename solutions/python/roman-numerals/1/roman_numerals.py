"""Module to implement Arabic to Roman numerals conversion."""
# Dictionary mapping Arabic values to their Roman numeral symbols.
# Ordered from largest to smallest, as required by the greedy algorithm.
BASE_SYMBOLS = {
    1000: 'M', 500: 'D', 100: 'C',
    50: 'L', 10: 'X', 5: 'V', 1: 'I'
}


def get_contraction_rules(symbols):
    # Build the list of substitution rules to fix illegal repetitions.
    # For each symbol, two rules are generated:
    #   1. Four consecutive symbols => subtractive form (e.g. IIII => IV)
    #   2. Pattern like VIV => IX, which arises after applying rule 1
    rules = []
    for idx in range(len(symbols) - 1, 0, -1):
        curr = symbols[idx]
        supp = symbols[idx - 1]
        rules.append((curr * 4, curr + supp))
        if idx > 1:
            supp_again = symbols[idx - 2]
            rules.append((supp + curr + supp, curr + supp_again))
    return rules

def roman(number):
    # Greedy loop: subtract the largest possible value at each step,
    # appending the corresponding symbol to the result.
    result = ""
    remaining = number
    for value, symbol in BASE_SYMBOLS.items():
        while remaining >= value:
            result += symbol
            remaining -= value
    # Apply contraction rules to replace illegal sequences with their
    # correct subtractive forms (e.g. IIII => IV, DCCCC => CM).
    symbol_list = list(BASE_SYMBOLS.values())
    for illegal, legal in get_contraction_rules(symbol_list):
        result = result.replace(illegal, legal)
    return result