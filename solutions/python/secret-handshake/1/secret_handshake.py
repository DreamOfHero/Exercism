POSSIBLE_ACTIONS = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    actions = []
    inverted_binary = binary_str[::-1]
    pos_last_char = len(inverted_binary) - 1
    for idx in range(pos_last_char):
        if inverted_binary[idx] == "1":
            actions.append(POSSIBLE_ACTIONS[idx])
    if inverted_binary[pos_last_char] =="1":
        actions = actions[::-1]
    return actions