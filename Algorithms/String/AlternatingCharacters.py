# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true
# Difficulty: Easy

# Complexity: Time - O(n) and Space: O(n)


def alternatingCharacters(s):
    # Write your code here
    stack = []
    stack.append(s[0])
    
    count = 0
    
    for char in s[1:]:
        if len(stack) > 0 and stack[-1] == char:
            count += 1
        else:
            stack.append(char)
    
    return count
    
