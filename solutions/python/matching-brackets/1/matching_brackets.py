OPENED_BRACKETS = "([{"
CLOSED_BRACKETS = "}])"
# Map closing brackets to their corresponding opening partners
PAIRS_BRACKETS = {')': '(', ']': '[', '}': '{'}

def is_paired(input_string):
    stack = []
    for char in input_string:
        # If it's an opening bracket, push it onto the stack
        if char in OPENED_BRACKETS:
            stack.append(char)
        # If it's a closing bracket, we must validate it
        elif char in CLOSED_BRACKETS:
            # Check if stack is empty (no opening bracket) 
            # or if the last opened bracket doesn't match
            if not stack or stack[-1] != PAIRS_BRACKETS[char]:
                return False
            # Match found, remove the opening bracket from the stack
            stack.pop()
    # If the stack is empty, all brackets were correctly paired
    return not stack