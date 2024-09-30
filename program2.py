class Solution(object):
def roman_to_int(s: str) -> int:
    # Define the Roman numeral values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    length = len(s)

    for i in range(length):
        # Get the value of the current symbol
        value = roman_values[s[i]]
        
        # Check if the next symbol exists and is larger
        if i + 1 < length and roman_values[s[i + 1]] > value:
            total -= value  # Subtract if the next symbol is larger
        else:
            total += value  # Otherwise, add the value
    
    return total


