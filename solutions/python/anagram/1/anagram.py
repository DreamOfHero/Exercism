def find_anagrams(word, candidates):
    """
    Find candidate words that are anagrams of the target word.
    """
    # 1. Prepare the target word: lowercase it and sort its letters
    target_lower = word.lower()
    target_sorted = sorted(target_lower)
    
    # 2. Initialize an empty list to store the results
    anagrams_found = []
    
    # 3. Iterate through each candidate in the provided list
    for candidate in candidates:
        candidate_lower = candidate.lower()
        
        # 4. Check the two rules:
        # - The candidate must not be the exact same word as the target
        # - The candidate must have the exact same sorted letters as the target
        if candidate_lower != target_lower and sorted(candidate_lower) == target_sorted:
            # 5. If both conditions are met, add the original candidate to our list
            anagrams_found.append(candidate)
            
    # 6. Return the final list of identified anagrams
    return anagrams_found