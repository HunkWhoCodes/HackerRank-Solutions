# https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true
# Difficulty: Easy

# Complexity - Time: O(n) and Space: O(n)


def pangrams(s):
    # Write your code here
    p = s.lower()
    
    alphabets = [chr(val) for val in range(ord("a"), ord("a") + 26)]
    freq = Counter(p)
    
    for c in alphabets:
        if c not in freq:
            print(c)
            return "not pangram"
    
    return "pangram"
