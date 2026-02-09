def create_poem_parts():
    """
    Returns a list of tuples containing the subject and the action 
    for each part of the nursery rhyme.
    """
    parts = []
    # Index 0 is the base of the rhyme (the house)
    parts.append(("house", "Jack built"))
    parts.append(("malt", "lay in"))
    parts.append(("rat", "ate"))
    parts.append(("cat", "killed"))
    parts.append(("dog", "worried"))
    parts.append(("cow with the crumpled horn", "tossed"))
    parts.append(("maiden all forlorn", "milked"))
    parts.append(("man all tattered and torn", "kissed"))
    parts.append(("priest all shaven and shorn", "married"))
    parts.append(("rooster that crowed in the morn", "woke"))
    parts.append(("farmer sowing his corn", "kept"))
    parts.append(("horse and the hound and the horn", "belonged to"))
    return parts

def create_verse(poem_parts, index):
    """
    Constructs a single cumulative verse based on the given index.
    """
    # Initialize the verse with the primary subject for this stanza
    created_verse = f"This is the {poem_parts[index][0]}"
    
    # Iterate backwards from the current index down to the second element (index 1)
    # linking each subject to the action performed on the previous one.
    for back in range(index, 0, -1):
        action = poem_parts[back][1]
        previous_subject = poem_parts[back - 1][0]
        created_verse += f" that {action} the {previous_subject}"
    
    # Every verse must end with the final reference to Jack's house
    created_verse += f" that {poem_parts[0][1]}."
    
    return created_verse

def recite(start_verse, end_verse):
    """
    Generates a range of verses from start_verse to end_verse.
    """
    poem_parts = create_poem_parts()
    recited_verses = []
    
    # Range includes end_verse; we subtract 1 from verse_number for 0-based indexing
    for verse_number in range(start_verse, end_verse + 1):
        single_verse = create_verse(poem_parts, verse_number - 1)
        recited_verses.append(single_verse)
        
    return recited_verses