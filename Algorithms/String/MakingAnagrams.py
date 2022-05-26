# https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true
# Difficulty: Easy, Points: 25

# Compleity - Time: O(n) and Space: O(n)

# Count frequency of each letter in 2 counters for both strings and then calculate the value of common keys
# Finally calculate the total length of s1 and s2 and subtract 2* this common length. We'll find useless characters
# That we can remove. 2 times of common because these would be present in btoh strings and count towards the anagram. 

def makingAnagrams(s1, s2):
    freq1 = Counter(s1)
    freq2 = Counter(s2)
    
    common_len = 0
    for k, v in freq1.items():
        if k in freq2:
            common_len += min(freq1[k], freq2[k])
    
    total_len = len(s1) + len(s2)
    ans = total_len - 2 * common_len
    
    return ans
