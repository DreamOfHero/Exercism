def append(list1, list2):
    # Start with the first list
    result = list1
    # Iterate through every element of the second list
    for element in list2:
        # Add the element to the end by creating a new combined list
        result = result + [element]
    return result

def concat(lists):
    # Initialize an empty list to store all elements
    result = []
    # Iterate through the series of provided lists
    for lst in lists:
        # For each list, iterate through its individual elements
        for element in lst:
            # Flatten the structure by adding each element to the final list
            result = result + [element]
    return result

def filter(function, lst):
    # List to collect elements that satisfy the condition
    result = []
    # Examine each element in the original list
    for element in lst:
        # If the predicate function returns True for the element
        if function(element):
            # Add it to the result list
            result = result + [element]
    return result

def length(lst):
    # Initialize a counter at zero
    count = 0
    # Iterate through the list (using _ as the element itself isn't needed)
    for _ in lst:
        # Increment the counter for each item found
        count += 1
    return count

def map(function, lst):
    # List to collect the results of the transformation
    result = []
    # Iterate through every element of the list
    for element in lst:
        # Apply the function and add the result to the new list
        result = result + [function(element)]
    return result

def foldl(function, lst, initial):
    # Start with the initial value (accumulator)
    accumulator = initial
    # Iterate through the list from left to right
    for element in lst:
        # Update the accumulator by applying the function
        accumulator = function(accumulator, element)
    return accumulator

def foldr(function, lst, initial):
    # Start with the initial value (accumulator)
    accumulator = initial
    # Reverse the list to process it "from the right"
    reversed_list = reverse(lst)
    # Iterate through the reversed list
    for element in reversed_list:
        # Update the accumulator by applying the function
        accumulator = function(accumulator, element)
    return accumulator

def reverse(lst):
    # Initialize an empty list
    result = []
    # Iterate through each element of the original list
    for element in lst:
        # Insert the CURRENT element BEFORE the existing result list
        # This naturally reverses the order
        result = [element] + result
    return result