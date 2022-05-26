# https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true
# Difficulty: Easy, Points: 30

# Complexity - Time: O(n) and Space: O(1)



def gameOfThrones(s):
    # Write your code here
    n = len(s)
    
    if n <= 1:
        return "YES"
    
    freq = Counter(s)
    
    one_len = 0
    odd_len = 0
    
    for k, v in freq.items():
        if v == 1:
            one_len += 1
        elif v % 2 != 0:
            odd_len += 1

    if one_len == 0 and odd_len == 0:
        return "YES"
    elif one_len == 1 and odd_len == 0:
        return "YES"
    elif one_len == 0 and odd_len == 1:
        return "YES"
    else:
        return "NO"
        
