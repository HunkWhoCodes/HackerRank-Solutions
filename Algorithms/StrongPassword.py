# https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true
# Difficulty: Easy

# Complexity: O(n)

# def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    special_characters = "!@#$%^&*()-+"
    special_chars = list(special_characters)
    
    upper = lower = digit = special =  1
    for c in password:
        if c.isalpha():
            if c.isupper():
                upper = 0
            if c.islower():
                lower = 0
        elif c.isdigit():
            digit = 0
        elif c in special_chars:
                special = 0
    
    remains = upper + lower + digit + special   # Remaining Conditions
    
    short = 0
    if 6 - n > 0:
        short = 6 - n           # If we are short of 6 chars, then short = 6 - n
        
    if remains >= short:
        return remains
    elif remains < short:
        return short
    
    # return max(remains, short)
                
