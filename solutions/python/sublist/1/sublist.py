# Possible sublist categories
UNEQUAL = -99
SUBLIST = -1
EQUAL = 0
SUPERLIST = 1

def sublist(list_one, list_two):
    # Handle empty list scenarios first for logical priority
    if not list_one and not list_two:
        return EQUAL
    elif not list_one:
        return SUBLIST
    elif not list_two:
        return SUPERLIST

    # Store the result of the containment check in descriptive booleans
    list_one_in_two = is_contained_in(list_one, list_two)
    list_two_in_one = is_contained_in(list_two, list_one)

    # Comparison logic based on length and presence
    if len(list_one) == len(list_two) and list_one_in_two:
        return EQUAL
    
    elif len(list_one) < len(list_two) and list_one_in_two:
        return SUBLIST
    
    elif len(list_two) < len(list_one) and list_two_in_one:
        return SUPERLIST
        
    return UNEQUAL
    
def is_contained_in(small_list, large_list):
    # Determine the number of possible starting positions for the sliding window
    possible_positions = len(large_list) - len(small_list) + 1
    
    for i in range(possible_positions):
        # Compare the current slice of the large list with the small list
        if large_list[i : i + len(small_list)] == small_list:
            return True
            
    return False