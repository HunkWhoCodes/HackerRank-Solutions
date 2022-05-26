# https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true
# Difficulty: Easy, Points: 25

# Complexity - Time: O(n) and Space: O(n)

# Need to find if they have a common substring. Even if 1 char is common then they have a common substring.
# Substring vs Subsequence:
# Subsequence -> Order Matters. Relevant problem is Longest Common Substring
# Substring -> Order does not matter.

def twoStrings(s1, s2):
    freq1, freq2  = Counter(s1), Counter(s2)
    
    for k,v in freq1.items():
        if k in freq2:
            return "YES"
    
    return "NO"
