def abbreviate(words):
    # Replace hyphens with spaces to treat them as word separators
    splitted_words = words.replace("-", " ").split()
    acronym = []
    
    for word in splitted_words:
        # Find the first alphabetic character in the word
        for char in word:
            if char.isalpha():
                acronym.append(char.upper())
                # Stop searching once the first letter of the word is found
                break
                
    return "".join(acronym)