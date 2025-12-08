def valid_structure(isbn):
    """Return True if ISBN-10 has valid format, False otherwise."""
    # ISBN must be exactly 10 characters
    if len(isbn) != 10:
        return False
    
    # First 9 characters must be digits
    if not isbn[:9].isdigit():
        return False
    
    # Last character must be a digit or 'X'
    if not (isbn[9].isdigit() or isbn[9] == "X"):
        return False
    
    return True


def is_valid(isbn):
    """Return True if ISBN-10 is valid, False otherwise."""
    # Remove any dashes for processing
    only_numbers = isbn.replace("-", "")
    
    # Check if the structure of ISBN is correct
    if not valid_structure(only_numbers):
        return False 
    
    # Calculate the checksum using the ISBN-10 formula
    checksum = 0
    for weight in range(10, 0, -1):
        index = len(only_numbers) - weight
        # Convert 'X' to 10 for checksum calculation
        number = 10 if only_numbers[index] == "X" else int(only_numbers[index])
        checksum += number * weight
    
    # Valid if checksum is divisible by 11
    return checksum % 11 == 0