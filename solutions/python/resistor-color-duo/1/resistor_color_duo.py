# List of resistor colors in order of their numeric values
COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


def value(colors):
    """Return the resistance value from the first two color bands."""
    # The first color represents the tens digit,
    # the second color represents the ones digit
    return color_code(colors[0]) * 10 + color_code(colors[1])


def color_code(color):
    """Return the numeric value associated with a resistor color."""
    # The value corresponds to the index of the color in the COLORS list
    return COLORS.index(color)