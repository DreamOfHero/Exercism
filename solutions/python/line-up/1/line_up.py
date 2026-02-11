def line_up(name, number):
    """
    Generates a welcome sentence with the name and the correct ordinal number.
    """
    # Convert number to string to easily access digits by position
    str_num = str(number)
    last_char = str_num[-1]
    last_two_char = ""
    
    # Check if the number has at least two digits to identify exceptions (11, 12, 13)
    if len(str_num) >= 2:
        last_two_char = str_num[-2:]
    
    # Apply ordinal suffix rules based on the last digit and the "teen" exceptions
    if last_char == "1" and last_two_char != "11":
        str_num += "st"
    elif last_char == "2" and last_two_char != "12":
        str_num += "nd"
    elif last_char == "3" and last_two_char != "13":
        str_num += "rd"
    else:
        # All other numbers, including 11, 12, and 13, use "th"
        str_num += "th"
    
    # Return the formatted English sentence
    return f"{name}, you are the {str_num} customer we serve today. Thank you!"