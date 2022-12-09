#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
score = 0

for line in data:
    f, s = line[:len(line)//2], line[len(line)//2:]

    c = None
    for i in f:
        if i in s:
            c = i
    score += ord(c) - ord('a') + 1
    if ord('A') <= ord(c) and ord(c) <= ord('Z'):
        score += ord('a') - ord('A') + 26
print(score)


# Part 2
score = 0

for i in range(0,len(data), 3):
    c = None
    for x in data[i]:
        if x in data[i+1] and x in data[i+2]:
            c = x
    score += ord(c) - ord('a') + 1
    if ord('A') <= ord(c) and ord(c) <= ord('Z'):
        score += ord('a') - ord('A') + 26
print(score)