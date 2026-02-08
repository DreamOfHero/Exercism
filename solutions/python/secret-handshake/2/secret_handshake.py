# List of actions mapped to the binary positions 1-4
POSSIBLE_ACTIONS = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    """
    Decode a binary string into a secret handshake sequence.
    """
    actions = []
    # Reverse the string to process bits from right to left using list indexing
    inverted_binary = binary_str[::-1]
    
    # Identify the index of the control bit (the 5th bit)
    pos_last_char = len(inverted_binary) - 1
    
    # Build the action list based on the first four bits
    for idx in range(pos_last_char):
        if inverted_binary[idx] == "1":
            actions.append(POSSIBLE_ACTIONS[idx])
    
    # Check the 5th bit to determine if the sequence should be reversed
    if inverted_binary[pos_last_char] == "1":
        actions.reverse()
        
    return actions