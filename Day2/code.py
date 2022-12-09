#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
ans = 0
for line in data:
    a, b = line.split(' ')
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')
    ans += b + 1
    if a == b:
        ans += 3
    if (a+1) % 3 == b:
        ans += 6
print(ans)

# Part 2
ans = 0
for line in data:
    a, b = line.split(' ')
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')
    if b == 0:
        ans += (a+2)%3 + 1
    if b == 1:
        ans += a + 4
    if b == 2:
        ans += (a+1)%3 + 7
print(ans)