import string

def is_pangram(sentence):
    """
    Check if a sentence is a pangram.
    
    A pangram contains every letter of the alphabet at least once.
    Case insensitive.
    
    Args:
        sentence: String to check
    
    Returns:
        True if pangram, False otherwise
    """
    # Counter for found alphabet letters
    letters_found = 0
    
    # Get all 26 lowercase English letters
    english_letters = string.ascii_lowercase
    
    # Extract unique letters from sentence (case insensitive)
    unique_letters = set(sentence.lower())
    
    # Check each alphabet letter
    for letter in english_letters:
        if letter in unique_letters:
            letters_found += 1
    
    # Pangram must contain all 26 letters
    return letters_found == len(english_letters)