def square_of_sum(number):
    # Initialize a counter for the sum of natural numbers
    total_sum = 0
    # Iterate from 1 up to and including the given number
    for natural_number in range(1, number + 1):
        total_sum += natural_number
    # Return the square of the accumulated sum
    return total_sum ** 2

def sum_of_squares(number):
    # Initialize a counter for the sum of squared numbers
    total_sum = 0
    # Iterate from 1 up to and including the given number
    for natural_number in range(1, number + 1):
        # Square each number before adding it to the total
        total_sum += natural_number ** 2
    return total_sum

def difference_of_squares(number):
    # Calculate both values separately and store them in descriptive variables
    total_sum = sum_of_squares(number)
    total_square = square_of_sum(number)
    
    # Subtract the sum of squares from the square of the sum
    # (The square of the sum is always larger or equal for natural numbers)
    return total_square - total_sum