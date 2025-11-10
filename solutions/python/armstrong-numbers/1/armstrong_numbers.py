def is_armstrong_number(number):
    str_number = str(number)               # convert the number to a string to iterate over its digits
    armstrong_number = 0                   # initialize the sum of powers
    for char in str_number:                # loop through each digit in the number
        armstrong_number += int(char) ** len(str_number)  # raise digit to the number of digits and add to sum
    return armstrong_number == number      # check if the sum equals the original number
