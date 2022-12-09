#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read()

def solve(data, k):
    score = 0
    for i in range(len(data)-k):
        good = True
        mp = set()
        for j in range(k):
            if data[j+i] in mp:
                good = False
                break
            mp.add(data[j+i])
        if good:
            score = i + k
            break
    return score

# Part 1
print(solve(data, 4))

# Part 2
print(solve(data, 14))