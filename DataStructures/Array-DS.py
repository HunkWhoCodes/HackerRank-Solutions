# https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true
# Difficulty: Easy, Points: 10

# Complexity: Time: O(n) and Space: O(n)


def reverseArray(a):
    rev = []
    
    for i in range(len(a) -1, -1, -1):
        rev.append(a[i])
    
    return rev
    # One line Python:
    # return a[::-1]
