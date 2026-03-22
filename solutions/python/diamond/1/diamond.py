import string

ALPHABET = string.ascii_uppercase

def rows(letter):
    rows_array = []
    # Position of the target letter (e.g., 'C' -> 2)
    letter_pos = ALPHABET.find(letter)
    # Total width and height of the diamond (must be odd)
    width = 2 * letter_pos + 1
    
    for index_row in range(width):
        # Calculate how far we are from the middle row
        distance = abs(letter_pos - index_row)
        # The character is determined by the distance from the target letter
        char = ALPHABET[letter_pos - distance]
        
        # Create a blank row of spaces
        row = [" "] * width
        # Place the character symmetrically from both ends
        row[distance] = char
        row[width - distance - 1] = char
        
        # Convert list to string and store
        rows_array.append("".join(row))
        
    return rows_array