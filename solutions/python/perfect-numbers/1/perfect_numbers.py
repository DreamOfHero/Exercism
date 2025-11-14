import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Only positive integers can be classified
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    # Collect all divisors except the number itself
    divisors = []
    
    # 1 is a divisor for all numbers except 1 itself
    if number != 1:
        divisors.append(1)
    
    # Check divisors up to square root for efficiency
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            # Add the divisor
            divisors.append(divisor)
            # Add its complement (the other factor of the division)
            other_divisor = number // divisor
            # Avoid duplicates for perfect squares
            if other_divisor != divisor:
                divisors.append(other_divisor)
    
    # Calculate aliquot sum
    total = sum(divisors)
    
    # Classify based on comparison with aliquot sum
    if number < total:
        return "abundant"
    elif number > total:
        return "deficient"
    else:
        return "perfect"