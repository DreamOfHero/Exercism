def transform(legacy_data):
    # Initialize an empty dictionary for the new one-to-one mapping
    result = {}
    # Iterate through the old dictionary (score is the key, list of chars is the value)
    for score, chars in legacy_data.items():
        # Iterate through each character in the current score group
        for char in chars:
            # Convert character to lowercase as requested
            lower_char = char.lower()
            # Map the individual letter directly to its point value
            result[lower_char] = score
    return result