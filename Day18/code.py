#!/usr/bin/env python3
import sys
sys.setrecursionlimit(30000)

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

s = set()
for i in data:
    s.add(tuple(map(int, i.split(','))))

# Part 1
ans = 0
for i in data:
    v = tuple(map(int, i.split(',')))
    for i in range(-1,2):
        if not tuple([v[0]+i, v[1], v[2]]) in s:
            ans += 1
        if not tuple([v[0], v[1]+i, v[2]]) in s:
            ans += 1
        if not tuple([v[0], v[1], v[2]+i]) in s:
            ans += 1
print(ans)

# Part 2
ans = 0
MN, MX = -1, 21
visited = set()

def getSides(i, j, k):
    cnt = 0
    for x in range(-1,2):
        if x == 0:
            continue
        if tuple([i+x, j, k]) in s:
            cnt += 1
        if tuple([i, j+x, k]) in s:
            cnt += 1
        if tuple([i, j, k+x]) in s:
            cnt += 1
    return cnt

def dfs(i, j, k):
    global ans
    tup = tuple([i, j, k])
    if (tup in visited) or (tup in s) or (min(i,j,k) < MN) or (max(i,j,k) > MX):
        return
    visited.add(tup)
    ans += getSides(i,j,k)
    dfs(i+1,j,k)
    dfs(i-1,j,k)
    dfs(i,j+1,k)
    dfs(i,j-1,k)
    dfs(i,j,k+1)
    dfs(i,j,k-1)
dfs(0,0,0)
print(ans)