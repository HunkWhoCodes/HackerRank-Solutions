def countingValleys(steps, path):
    # Write your code here
    temp = [0] * steps
    
    current = 0
    for i, s in enumerate(path):
        if s == "U":
            current += 1
        elif s == "D":
            current -= 1
        temp[i] = current
    
    
    valleys, current = 0, 1
    
    while current < steps:
        if temp[current] < 0 and temp[current - 1] >= 0:
            valleys += 1
        current += 1
    
    if temp[0] < 0:
        valleys += 1
            
    return valleys
