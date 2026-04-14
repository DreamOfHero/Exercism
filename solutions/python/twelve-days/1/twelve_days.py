"""Module to implement the Twelve Days of Christmas song generator."""

# Dictionary mapping each day to its ordinal and corresponding gift.
full_song = {
    1: ("first", "a Partridge in a Pear Tree"),
    2: ("second", "two Turtle Doves"),
    3: ("third", "three French Hens"),
    4: ("fourth", "four Calling Birds"),
    5: ("fifth", "five Gold Rings"),
    6: ("sixth", "six Geese-a-Laying"),
    7: ("seventh", "seven Swans-a-Swimming"),
    8: ("eighth", "eight Maids-a-Milking"),
    9: ("ninth", "nine Ladies Dancing"),
    10: ("tenth", "ten Lords-a-Leaping"),
    11: ("eleventh", "eleven Pipers Piping"),
    12: ("twelfth", "twelve Drummers Drumming")
}


def create_verse(day):
    # Start the verse with the correct day header.
    current_verse = [f"On the {full_song[day][0]} day of Christmas my true love gave to me: "]

    # Add gifts in descending order, from the current day down to the first.
    # Each gift is followed by a comma and a space.
    for index_row in range(day, 0, -1):
        current_verse.append(full_song[index_row][1] + ", ")

    last_verse = len(current_verse) - 1

    # From the second day onward, the last gift requires "and" in front of it.
    if len(current_verse) > 2:
        current_verse[last_verse] = "and " + current_verse[last_verse]

    # Replace the trailing comma and space with the verse's final period.
    current_verse[last_verse] = current_verse[last_verse][:-2] + "."

    return "".join(current_verse)


def recite(start_verse, end_verse):
    # Build and return the list of verses for the requested range.
    requested_verses = []
    for verse_num in range(start_verse, end_verse + 1):
        requested_verses.append(create_verse(verse_num))
    return requested_verses