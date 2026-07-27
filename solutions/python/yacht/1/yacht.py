"""Module to implement scoring for the Yacht dice game."""

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def analyze_dice(dice):
    # Count occurrences of each die value.
    # Returns the counts dict and a sorted list of frequencies (descending),
    # which is used to identify patterns like Full House [3, 2] or Yacht [5].
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1
    return counts, sorted(counts.values(), reverse=True)


def score(dice, category):
    counts, sequence_frequency = analyze_dice(dice)

    if category == YACHT and sequence_frequency == [5]:
        # All five dice show the same face.
        return 50
    elif category in {ONES, TWOS, THREES, FOURS, FIVES, SIXES}:
        # The category constant equals the face value (1-6),
        # so it can be used directly for counting and multiplying.
        return dice.count(category) * category
    elif category == FULL_HOUSE and sequence_frequency == [3, 2]:
        # Exactly three of one value and two of another — Yacht excluded
        # because its frequency is [5], not [3, 2].
        return sum(dice)
    elif category == FOUR_OF_A_KIND:
        # Find the first die value that appears at least four times.
        # A Yacht (five of a kind) satisfies this condition too.
        for value, n in counts.items():
            if n >= 4:
                return value * 4
    elif category == LITTLE_STRAIGHT and sorted(dice) == [1, 2, 3, 4, 5]:
        return 30
    elif category == BIG_STRAIGHT and sorted(dice) == [2, 3, 4, 5, 6]:
        return 30
    elif category == CHOICE:
        # Any combination — just sum all dice.
        return sum(dice)

    # Dice do not satisfy the category requirements.
    return 0