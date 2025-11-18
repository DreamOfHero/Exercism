def is_isogram(string):
    """
    Check if a word or phrase is an isogram.
    
    An isogram has no repeating letters.
    Spaces and hyphens can appear multiple times.
    Case insensitive.
    
    Args:
        string: Word or phrase to check
    
    Returns:
        True if isogram, False otherwise
    """
    # Convert to lowercase list for comparison
    chars = list(string.lower())
    
    # Check each character
    for idx_a in range(len(chars)):
        # Only check alphabetic characters
        if chars[idx_a].isalpha():
            # Compare with all other characters
            for idx_b in range(len(chars)):
                # If same letter found at different position
                if idx_a != idx_b and chars[idx_a] == chars[idx_b]:
                    return False
    
    # No repeating letters found
    return True