def encode(string):
    # Add a sentinel character to avoid handling the last group separately
    string += "\0"
    encoded = []
    count = 1
    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            count += 1
        else:
            if count == 1:
                # Just the character for single occurrences
                encoded.append(string[index - 1])
            else:
                # Count plus character for repeats
                encoded.append(str(count) + string[index - 1])
                 # Reset the counter. Only if > 1
                count = 1
    return "".join(encoded)

def get_number(string, index):
    num = ""
    idx = index
    # Accumulate digits for multi-digit counts
    while string[idx].isdigit():
        num += string[idx]
        idx += 1
    return num

def decode(string):
    if not string:
        return ""
    index = 0
    decoded = []
    while index < len(string):
        number = get_number(string, index)
        if number != "":
            # Expand repeated characters directly
            decoded.append(string[index + len(number)] * int(number))
            index += len(number) + 1
        else:
            # Single character case
            decoded.append(string[index])
            index += 1
            
    return "".join(decoded)