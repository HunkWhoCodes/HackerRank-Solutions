# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true
# Difficulty: Easy, Points: 20

# Complexity: Time : O(n) and Space: O(1)


def squares(a, b):
    result = 0
    s_a = int(math.sqrt(a))
    s_b = int(math.sqrt(b))
    
    for n in range(s_a, s_b+1):
        sq = n *n
        # Check if sq is a whole number and within range
        if (sq - int(sq)) == 0 and sq >= a and sq <= b:
            result += 1
    
    return result
