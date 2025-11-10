def is_question(hey_bob):
    return hey_bob.strip().endswith("?")  # check if the input ends with a question mark, ignoring leading/trailing spaces

def is_yelling(hey_bob):
    is_alphabetical = any(char.isalpha() for char in hey_bob.strip())  # check if there is at least one letter
    return hey_bob == hey_bob.upper() and is_alphabetical              # yelling: all letters uppercase

def response(hey_bob):
    if is_yelling(hey_bob) and is_question(hey_bob):
        return "Calm down, I know what I'm doing!"  # combination of yelling and question
    if is_yelling(hey_bob):
        return "Whoa, chill out!"                  # yelling only
    if is_question(hey_bob):
        return "Sure."                             # question only
    if len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"                # silence
    return "Whatever."                             # any other input