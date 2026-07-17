"""Module to implement a D&D character generator with random ability scores."""
import random


def modifier(score):
    # Calculate the ability modifier: floor((score - 10) / 2).
    # Integer division in Python floors automatically for positive numbers,
    # but also works correctly for negative numbers (e.g. (3-10)//2 = -4).
    return (score - 10) // 2


def roll_die():
    # Simulate a single 6-sided die roll.
    # Kept outside Character because a die is a concept independent of a character.
    return random.randint(1, 6)


class Character:
    def __init__(self):
        # Each ability is rolled once and stored as an attribute.
        # Storing the result ensures the value never changes between accesses.
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        # Hitpoints depend on constitution, so they are calculated last.
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        # Roll 4 dice, sort ascending, discard the lowest (index 0),
        # and return the sum of the remaining three.
        dice = []
        for _ in range(4):
            dice.append(roll_die())
        dice.sort()
        return sum(dice[1:])