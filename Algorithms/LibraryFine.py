# https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true
# Difficulty: Easy, Points: 20

# Complexity - Time: O(n) and Space: O(1)

import datetime

def libraryFine(d1, m1, y1, d2, m2, y2):
    return_date = datetime.datetime(y1,m1,d1)
    due_date = datetime.datetime(y2, m2, d2)
    
    if return_date.year > due_date.year:
        return 10000
    if return_date.year == due_date.year and return_date.month > due_date.month:
        return 500 * (m1 - m2)
    if return_date.year == due_date.year and return_date.month == due_date.month and return_date > due_date:
        return 15 * (d1 - d2)
    if return_date <= due_date:
        return 0
    
# Same code without using datetime object attributes for months and years (Fails for some date based test cases, need to handle date edge cases better)
'''
def libraryFine(d1, m1, y1, d2, m2, y2):
    return_date = datetime.datetime(y1,m1,d1)
    due_date = datetime.datetime(y2, m2, d2)
    
    if y1 > y2:
        return 10000
    if y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    if y1 == y2 and m1 == m2 and return_date > due_date:
        return 15 * (d1 - d2)
    if return_date <= due_date:
        return 0
'''
