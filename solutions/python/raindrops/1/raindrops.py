def convert(number):
    """
    Convert a number into its corresponding raindrop sounds.
    
    Args:
        number: Integer to convert
    
    Returns:
        String with sounds or the number itself
    """
    # Map divisors to their corresponding sounds
    music_sheet = {3: "Pling", 5: "Plang", 7: "Plong"}
    
    # Accumulate sounds
    sounds = ""
    
    # Check each divisor
    for key, note in music_sheet.items():
        if number % key == 0:
            sounds += note
    
    # Return number as string if no sounds found
    if not sounds:
        sounds = str(number)
    
    return sounds