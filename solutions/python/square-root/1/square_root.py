def square_root(number):
    # We start our approximation with the number itself
    approximation = number
    
    while True:
        # Heron's method formula to find a value closer to the actual root
        better_approximation = (approximation + number // approximation) // 2
        
        # In integer arithmetic, if the new value is not smaller, 
        # we have found the integer square root
        if better_approximation >= approximation:
            return approximation
            
        approximation = better_approximation