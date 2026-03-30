UNDER_20 = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

MAGNITUDES = ["", "", "thousand", "million", "billion", "trillion"]

def split_number(number):
    str_number = str(number)
    parts = []
    while str_number:
        parts.append(str_number[-3:])
        str_number = str_number[:-3]
    parts.reverse()
    return parts

def convert_part(part_number):
    result = ""
    int_part = int(part_number)
    
    if int_part == 0:
        return result
        
    # Hundreds
    if int_part >= 100:
        result += UNDER_20[int(part_number[0])] + " hundred "
        int_part = int(part_number[1:])
        
    # Tens and Units
    if int_part >= 20:
        result += TENS[int(part_number[1])]
        int_part = int(part_number[-1])
    
    if int_part > 0:
        if len(result) > 0 and result[-1] == "y":
            result += "-"
        result += UNDER_20[int_part]
        
    return result.strip()

def say(number):
    if number < 0 or number >= 1000000000000:
        raise ValueError("input out of range")
        
    if number == 0:
        return UNDER_20[0]
        
    result = ""
    parts_number = split_number(number)
    count_parts = len(parts_number)
    
    for part in parts_number:
        # Normalize to 3 digits (e.g., "1" -> "001")
        str_part = convert_part(part.zfill(3))
        
        if len(str_part) > 0: 
            result += str_part + " "
            # Add magnitude (thousand, million, etc.)
            magnitude = 
            if MAGNITUDES[count_parts]:
                result += MAGNITUDES[count_parts] + " "
            
        count_parts -= 1
        
    return " ".join(result.split()) # Clean up multiple spaces