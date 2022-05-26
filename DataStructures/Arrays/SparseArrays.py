# https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true
# Difficulty: Medium, Points: 25

# Complexity: Time - O(n) and Space: O(n)

def matchingStrings(strings, queries):
    freq1 = Counter(strings)
    
    result = [0] * len(queries)
    
    for i, q in enumerate(queries):
        if q in freq1:
            result[i] = freq1[q]
    
    return result



