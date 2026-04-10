def check_errors(series, length):
    """Validate input parameters and raise specific ValueErrors if constraints are violated."""
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length < 0: 
        raise ValueError("slice length cannot be negative")
    if length == 0: 
        raise ValueError("slice length cannot be zero")
    if len(series) < length: 
        raise ValueError("slice length cannot be greater than series length")

def slices(series, length):
    """Return all contiguous substrings of a given length from the input series."""
    # Perform pre-flight error checking
    check_errors(series, length)
    
    sliced = []
    # Calculate the number of possible windows: (Total Length - Slice Length + 1)
    for char in range(len(series) - length + 1):
        # Extract the contiguous window using Python slicing
        sliced.append(series[char: char + length])
        
    return sliced