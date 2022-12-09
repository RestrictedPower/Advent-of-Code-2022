#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
ans = 0
n = len(data)
for i in range(n):
    for j in range(n):
        vis = False
        
        tmp = True
        for k in range(i+1, n):
            tmp &= data[k][j] < data[i][j]
        vis |= tmp
        
        tmp = True
        for k in range(j+1, n):
            tmp &= data[i][k] < data[i][j]
        vis |= tmp
        
        tmp = True
        for k in range(0, i):
            tmp &= data[k][j] < data[i][j]
        vis |= tmp
        
        tmp = True
        for k in range(0, j):
            tmp &= data[i][k] < data[i][j]
        vis |= tmp

        if vis:
            ans += 1
print(ans)

# Part 2
ans = 0
for i in range(n):
    for j in range(n):
        vis = False
        score = 1

        cur = 0
        for k in range(i+1, n):
            cur = k-i
            if data[k][j] >= data[i][j]:
                break
        score *= cur

        cur = 0
        tmp = True
        for k in range(j+1, n):
            cur = k-j
            if data[i][k] >= data[i][j]:
                break
        score *= cur

        cur = 0
        tmp = True
        for k in reversed(range(0, i)):
            cur = i-k
            if data[k][j] >= data[i][j]:
                break
        score *= cur

        cur = 0
        tmp = True
        for k in reversed(range(0, j)):
            cur = j-k
            if data[i][k] >= data[i][j]:
                break

        score *= cur
        ans = max(ans, score)
print(ans)