def egg_count(display_value):
    count_one = 0
    
    # Process the number as long as there are bits set to 1
    while display_value > 0:
        # Check the last bit using a bitwise AND with 1
        count_one += display_value & 1
        
        # Shift bits to the right by one position to check the next bit
        display_value >>= 1
        
    return count_one