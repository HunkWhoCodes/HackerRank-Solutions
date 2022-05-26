# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true
# Difficulty: Medium, Points: 35

# Complexity: Time: O(n) and Space: O(n)

# VERY VERY BAD Solution, with lot of explicit edge case handling. Improve it.


def isValid(s):
    freq = Counter(s)
    lowest = min(freq.values())
    highest = max(freq.values())
    diff = highest - lowest
    print(freq)
    if lowest != 1 and diff > 1:
        return "NO"
   
    
    freq2 = Counter(freq.values())
    print(freq2)
    
    if len(freq2) > 2:
        return "NO"
    elif len(freq2) <=1:
        return "YES"
    elif len(freq2) == 2:
        k1, k2 = list(freq2.keys())[:2]
        
        if k1 == 1 and freq2[k1] > 1:
            return "NO"
        if k2 == 1 and freq2[k2] > 1:
            return "NO"
            
        if freq2[k1] == 1 or freq2[k2] == 1:
            return "YES"
        else:
            return "NO"
