# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
# Difficulty: Easy

# Complexity - Time: O(n) (confirm int to str to int conversion complexity)
# Space: O(1)


def beautifulDays(i, j, k):
    # Write your code here
    beautiful_days = 0
    
    for day in range(i, j + 1):
        rev = int((str(day)[::-1]))
        diff = abs(day - rev)
        if diff % k == 0:
            beautiful_days += 1
    
    return beautiful_days
    
