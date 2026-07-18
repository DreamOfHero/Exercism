"""Module to implement a robot name generator with unique name assignment."""
import random
import string

# Set of all names already assigned to robots.
# Using a set ensures O(1) lookup, keeping name generation fast
# even when most of the name space has been used.
used_name = set()


def random_letters(length):
    # Generate a string of random uppercase ASCII letters of the given length.
    return "".join(random.choices(string.ascii_uppercase, k=length))


def random_number(digits):
    # Generate a zero-padded random number string of the given digit count.
    # e.g. digits=3 can produce "007", "342", "999".
    return f"{random.randint(0, 10 ** digits - 1):0{digits}d}"


def generate_robot_name():
    # Keep generating candidates until a name not yet in use is found.
    # With 26^2 * 10^3 = 676,000 possible names, collisions are rare
    # unless the name space is nearly exhausted.
    while True:
        name = random_letters(2) + random_number(3)
        if name not in used_name:
            used_name.add(name)
            return name


class Robot:
    def __init__(self):
        # Assign a unique name immediately on creation.
        self._robot_name = generate_robot_name()

    @property
    def name(self):
        # Expose the name as a read-only property.
        return self._robot_name

    def reset(self):
        # Wipe the current name and assign a new unique one.
        # The old name remains in used_name and will never be reused.
        self._robot_name = generate_robot_name()