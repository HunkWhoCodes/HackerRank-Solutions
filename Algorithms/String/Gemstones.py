# https://www.hackerrank.com/challenges/gem-stones/problem?isFullScreen=true
# Same as https://leetcode.com/problems/find-common-characters/
# Difficulty: Easy

# Complexity - Time: O(n*m), where n is number of words and m is length of longest word
# Space: O(m)


def gemstones(arr):
    # Write your code here
    word1 = list(arr[0])
    
    for word in arr[1:]:
        new_word = []
        for char in word:
            if char in word1:
                new_word.append(char)
                word1.remove(char)
        word1 = new_word
    
    return len(word1)
