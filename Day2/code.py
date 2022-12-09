#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'



inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
score = 0

for line in data:
    a, b = line.split(' ')
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')
    
    score += b + 1
    if a == b:
        score += 3
    if (a+1) % 3 == b:
        score += 6

print(score)

# Part 2
score = 0

for line in data:
    a, b = line.split(' ')
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')

    if b == 0:
        score += (a+2)%3 + 1
    if b == 1:
        score += a + 4
    if b == 2:
        score += (a+1)%3 + 7
        
print(score)