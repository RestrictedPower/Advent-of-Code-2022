#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
score = 0

for line in data:
    l1,r1 = map(int, line.split(',')[0].split('-'))
    l2,r2 = map(int, line.split(',')[1].split('-'))

    inside = (l2<=l1 and r1<=r2) or (l1<=l2 and r2<=r1)
    if inside:
        score += 1
print(score)

# Part 2
score = 0

for line in data:
    l1,r1 = map(int, line.split(',')[0].split('-'))
    l2,r2 = map(int, line.split(',')[1].split('-'))

    overlap = not(r1<l2 or r2<l1)
    if overlap:
        score += 1
print(score)
