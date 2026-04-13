def square_root(number):
    """Calculate the integer square root using Heron's method."""
    approximation = number
    while True:
        better_approximation = (approximation + number // approximation) // 2
        if better_approximation >= approximation:
            return approximation
        approximation = better_approximation

def is_prime(number):
    """Check if a number is prime using the 6k +/- 1 optimization."""
    if number <= 1:
        return False
    if number <= 3:
        return True 
    # Eliminate multiples of 2 and 3 upfront
    if number % 2 == 0 or number % 3 == 0:
        return False
        
    limit = int(square_root(number)) + 1
    # Check numbers in the form of 6k +/- 1
    for i in range(5, limit, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

def prime(number):
    """Find the nth prime number."""
    if number < 1:
        raise ValueError("there is no zeroth prime")
        
    counter = 0
    next_number = 2
    last_prime = 0
    
    # Keep checking numbers until we reach the nth prime
    while not counter == number:
        if is_prime(next_number):
            last_prime = next_number
            counter += 1
        next_number += 1
        
    return last_prime