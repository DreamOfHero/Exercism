def factors(value):
    if value <= 1: 
        return []
        
    prime_factors = []
    divisor = 2
    
    # Only check up to the square root of the remaining value
    while divisor * divisor <= value:
        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
            
        # Optimization: after 2, only check odd numbers
        if divisor == 2:
            divisor += 1
        else:
            divisor += 2
            
    # If anything remains, it must be a prime factor
    if value > 1:
        prime_factors.append(value)
        
    return prime_factors