def two_fer(name="you"):
    # The 'name' parameter defaults to "you" if no argument is provided during the call.
    # We return the formatted string directly to avoid unnecessary memory allocation 
    # for local variables.
    return f"One for {name}, one for me."