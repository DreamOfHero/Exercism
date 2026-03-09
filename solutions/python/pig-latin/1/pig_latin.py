VOWELS = "aeiou"

def translate(text):
    text_words = text.split(" ")
    translated_words = [""] * len(text_words)

    for index in range(len(text_words)):
        current_word = text_words[index]
        
        # Rule 1: Starts with a vowel, or "xr", or "yt"
        if current_word[0] in VOWELS or current_word[:2] in ("xr", "yt"):
            translated_words[index] = current_word
        else:
            consonant_sequence = ""
            i = 0
            while i < len(current_word):
                # Rule 4: 'y' acts as a vowel after a consonant sequence
                if current_word[i] == 'y' and i > 0:
                    break
                # Check for regular vowels
                elif current_word[i] in VOWELS:
                    break
                # Rule 3: 'qu' sequence must be moved together
                elif current_word[i] == 'q' and i + 1 < len(current_word) and current_word[i+1] == 'u':
                    consonant_sequence += 'qu'
                    break
                # Rule 2: Collect regular consonants
                else:
                    consonant_sequence += current_word[i]
                    i += 1
            
            # Move the collected consonant sequence to the end
            translated_words[index] = current_word[len(consonant_sequence):] + consonant_sequence
        
        # All rules end with the "ay" sound
        translated_words[index] += "ay"
        
    return " ".join(translated_words)