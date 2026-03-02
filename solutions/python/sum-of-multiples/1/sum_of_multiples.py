def sum_of_multiples(limit, multiples):
    # We use a set to automatically handle the "remove duplicates" requirement
    unique_multiples = set()

    # Iterate through each magical item base value (factor)
    for factor in multiples:
        # If the factor is 0, it has no multiples less than the limit (except 0 itself)
        # and we must avoid division/modulo by zero errors.
        if factor == 0:
            continue
            
        # We generate multiples directly by using 'factor' as the step in range.
        # This starts at 'factor' and jumps straight to 'factor * 2', 'factor * 3', etc.
        for multiple in range(factor, limit, factor):
            # Each number generated this way is guaranteed to be a multiple
            unique_multiples.add(multiple)

    # Calculate the final sum of all unique numbers collected
    return sum(unique_multiples)