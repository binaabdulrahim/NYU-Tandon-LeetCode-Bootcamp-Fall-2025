'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.'''

def myAtoi(s):
    # Step 1: Remove leading whitespace
    s = s.lstrip()  # Fix: lstrip not lstripe
    
    # Step 2: Check if empty
    if not s:
        return 0
    
    # Step 3: Handle sign
    sign = 1      # Fix: default positive
    index = 0     # Fix: start at position 0
    
    if s[0] == '-':
        sign = -1
        index = 1
    elif s[0] == '+':
        sign = 1   # Fix: just 1, not +1
        index = 1
    
    # Step 4: Read digits
    result = 0
    
    while index < len(s):
        char = s[index]
        
        if char.isdigit():
            result = result * 10 + int(char)
            index += 1
        else:
            break
    
    # Step 5: Apply sign
    result = result * sign
    
    # Step 6: Clamp to 32-bit range
    if result > 2147483647:
        return 2147483647
    elif result < -2147483648:
        return -2147483648  # Fix: was -2147483647
    
    return result