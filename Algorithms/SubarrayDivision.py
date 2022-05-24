# Subarray Division or Birthday Bar Problem
# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
# Difficulty: Easy

def birthday(s, d, m):
    # Write your code here
    start = 0
    end = m - 1
    n = len(s)
    result = 0
    
    while start < n and end < n and start <= end:
        temp = s[start:end+1]
        if sum(temp) == d:
            result += 1
        
        start += 1
        end += 1
    
    return result 
