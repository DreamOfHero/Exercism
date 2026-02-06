# List of resistor colors in order of their numeric values
# The index of each color corresponds to its numeric value
COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]


def value(colors):
    """Return the base resistance value from the first two color bands."""
    # The first color represents the tens digit
    # The second color represents the ones digit
    return color_code(colors[0]) * 10 + color_code(colors[1])


def color_code(color):
    """Return the numeric value associated with a resistor color."""
    # The numeric value is given by the position of the color in COLORS
    return COLORS.index(color)


def label(colors):
    """Return the formatted resistance label with the correct unit."""
    # Build the full resistance value by appending zeros
    # determined by the third color band
    full_value = str(value(colors)) + ("0" * color_code(colors[2]))

    # Count how many trailing zeros the number has
    trailing_zeros = len(full_value) - len(full_value.rstrip("0"))

    # Reduce the number of zeros to the nearest multiple of 3
    # to match metric prefixes (kilo, mega, giga)
    unit_zeros = (trailing_zeros // 3) * 3

    # Convert the value back to an integer and scale it
    final_value = int(full_value) // (10 ** unit_zeros)

    # Map zero groups to their corresponding unit
    units = {
        0: "ohms",
        3: "kiloohms",
        6: "megaohms",
        9: "gigaohms",
    }

    return f"{final_value} {units[unit_zeros]}"
