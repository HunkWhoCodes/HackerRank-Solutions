# HackerRank in a String
# Same as https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy

# Complexity - Time: O(n), Space: O(1)


def hackerrankInString(s):
    # Write your code here
    H = "hackerrank"
    n = len(H)
    m = len(s)
    
    i, j = 0, 0
    
    while i < n and j < m :
        if H[i] == s[j]:
            i += 1
            j += 1
        else:
            j += 1
                
    if i == n:
        return "YES"
    else:
        return "NO"
