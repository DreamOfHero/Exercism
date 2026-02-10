def distance(strand_a, strand_b):
    """
    Calculates the Hamming distance between two DNA strands.
    """
    # Validation: Hamming distance is only defined for sequences of equal length.
    # This single check covers all cases of length mismatch, including empty strands 
    # being compared with non-empty ones.
    if len(strand_a) != len(strand_b): 
        raise ValueError("Strands must be of equal length.")
    
    # Initialize the difference counter.
    hamming = 0
    
    # Iterate through the strands using their index to compare nucleotides 
    # at the same position.
    for num in range(len(strand_a)):
        # If nucleotides differ, it's a point mutation; increment the distance.
        if strand_a[num] != strand_b[num]:
            hamming += 1
            
    # Return the final count of differences.
    # Note: if both strands are empty, the loop never runs and returns 0 correctly.
    return hamming