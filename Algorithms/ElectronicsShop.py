# Electronics Shop
# Difficulty: Easy
# https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

# Complexity: O(n^2)

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    
    max_cost = -1
    
    for k in keyboards:
        for d in drives:
            cost = k + d
            if cost <= b:
                max_cost = max(max_cost, cost)
    
    return max_cost
