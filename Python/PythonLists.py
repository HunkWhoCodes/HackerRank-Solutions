# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Easy, 10 points



if __name__ == '__main__':
    N = int(input())
    arr = []
    
    while N:
        inp = input()
        op = inp.split()
        if op[0] == "insert":
            ind = int(op[1])
            val = int(op[2])
            arr.insert(ind, val)
        elif op[0] == "print":
            print(arr)
        elif op[0] == "remove":
            v = int(op[1])
            arr.remove(v)
        elif op[0] == "append":
            a = int(op[1])
            arr.append(a)
        elif op[0] == "sort":
            arr.sort()
        elif op[0] == "pop":
            arr.pop()
        elif op[0] == "reverse":
            arr.reverse()
        N -= 1
