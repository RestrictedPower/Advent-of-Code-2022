#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n\n')

# Part 1
mx = 0
for x in data:
    v = sum([int(i) for i in x.split('\n')])
    mx = max(mx, v)
print(mx)

# Part 2
print(sum(sorted([(sum(int(j) for j in i.split('\n'))) for i in data])[-3:]))