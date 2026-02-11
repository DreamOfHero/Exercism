def flatten(iterable):
    """
    Returns a single flattened list from a nested structure, excluding None values.
    """
    flattened_array = []
    
    for element in iterable:
        # Check if the current element is a list to handle nesting
        if type(element) is list:
            # Recursively flatten the sub-list and extend the main array
            flattened_array.extend(flatten(element))
        else:
            # If it's a single value, add it only if it is not None
            if element is not None:
                flattened_array.append(element)
                
    return flattened_array