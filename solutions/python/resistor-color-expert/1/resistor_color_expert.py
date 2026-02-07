COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
TOLERANCE = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}

def color_value(colors):
    """Extract and combine the significant digits from the initial color bands."""
    result = 0
    for i in range(len(colors) - 2):
        result = result * 10 + color_code(colors[i])
    return result

def color_code(color):
    """Return the numerical index for a specific color band."""
    return COLORS.index(color)

def tolerance_percentage(color):
    """Retrieve the tolerance percentage value from the tolerance band."""
    return TOLERANCE[color]

def get_resistor_label(colors):
    """Calculate the total resistance and format it with the appropriate metric prefix."""
    full_value_int = color_value(colors) * (10 ** color_code(colors[-2]))
    
    units = [(1_000_000_000, "gigaohms"), (1_000_000, "megaohms"), (1_000, "kiloohms"), (1, "ohms")]
    
    for divisor, unit_name in units:
        if full_value_int >= divisor:
            final_value = full_value_int / divisor
            if final_value == int(final_value):
                final_value = int(final_value)
            return f"{final_value} {unit_name}"

def resistor_label(colors):
    """Main function to return the full resistor label including tolerance."""
    if len(colors) == 1:
        return "0 ohms"    
    return f"{get_resistor_label(colors)} ±{tolerance_percentage(colors[-1])}%"