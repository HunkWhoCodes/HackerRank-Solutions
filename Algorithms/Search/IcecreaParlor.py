# https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
# Difficulty: Easy, Points: 30

# Complexity - Time: O(n^2) and Space: O(1)

# Same as Two Sum

# This is a bruteforce quadratic time solution, use hash table for the O(n) one.



def icecreamParlor(m, arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i, n):
            if i != j and arr[i] + arr[j] == m:
                return [i+1, j+1]
