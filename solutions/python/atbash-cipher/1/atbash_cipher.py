import string

ALPHABET = string.ascii_lowercase
LEN_ALPHABET = len(ALPHABET) - 1

def choose_char(text, index):
    char = text[index].lower()
    if char.isdigit():
        return char
    elif char.isalpha():
        # Directly calculates the mirrored alphabet position
        return ALPHABET[LEN_ALPHABET - ALPHABET.index(char)]
    else:
        return ""

def encode(plain_text):
    encoded_text = ""
    for index in range(len(plain_text)):
        # Directly append the result of the translation
        encoded_text += choose_char(plain_text, index)
        
        # Check the length of the actual cipher characters (ignoring spaces)
        # If it's a multiple of 5, ensure exactly one space follows the block
        if len(encoded_text.replace(" ", "")) and len(encoded_text.replace(" ", "")) % 5 == 0:
            encoded_text = encoded_text.strip() + " "
            
    return encoded_text.strip()

def decode(ciphered_text):
    decoded_text = ""
    for index in range(len(ciphered_text)):
        # Simple linear accumulation for decoding
        decoded_text += choose_char(ciphered_text, index)
    return decoded_text