
# https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
# Difficulty: Easy, Points: 45

# Complexity: Time: O(n) and Space: O(n)

def missingNumbers(arr, brr):
    freq1, freq2 = Counter(arr), Counter(brr)
    missing = []
    
    for k, v in freq2.items():
        if k not in freq1:
            missing.append(k)
        elif k in freq1 and freq1[k] != freq2[k]:
            missing.append(k)
    
    missing.sort()
    return missing
