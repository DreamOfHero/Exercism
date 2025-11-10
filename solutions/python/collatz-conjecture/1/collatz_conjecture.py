def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")  # raise error for non-positive input
    to_one = number                                          # working copy of the number
    steps_collatz = 0                                        # initialize step counter
    while not to_one == 1:                                   # loop until number reaches 1
        if to_one % 2 == 0:
            to_one = to_one // 2                             # if even, divide by 2
        else:
            to_one = to_one * 3 + 1                         # if odd, multiply by 3 and add 1
        steps_collatz += 1                                   # count each operation as a step
    return steps_collatz                                      # return total number of steps
