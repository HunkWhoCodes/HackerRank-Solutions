# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Difficulty: Easy, Points; 10

# Solve with 2 pointers 

# Complexity: Time : O(N*m) where N is the length of the string and m is the length of max substring
# Complexity: Space: O(1)


def count_substring(string, sub_string):
    count = 0
    m = len(string)
    n = len(sub_string)
    
    i = 0
    j = n - 1
    
    while i < m and j < m and i < j:
        sub = string[i:j+1]
        if sub == sub_string:
            count += 1
        i += 1
        j += 1
    
    return count
