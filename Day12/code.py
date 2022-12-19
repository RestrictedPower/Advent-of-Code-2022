#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

def elev(c):
    if c == 'E': c = 'z'
    if c == 'S': c = 'a'
    return ord('z') - ord(c)

# Part 1
def p1():
    n, m, INF = len(data), len(data[0]), 100000000
    dist = [[INF for i in range(m)] for i in range(n)]
    q = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'S':
                q.append([i,j])
                dist[i][j] = 0
                break
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    def inside(i, j):
        return i<n and j<m and i>=0 and j>=0
    ans = 0
    while q:
        i, j = q.pop(0)
        for k in range(4):
            nI, nJ = i + dx[k], j + dy[k]
            if not inside(nI, nJ): continue 
            # print(nI,nJ)
            if dist[nI][nJ] != INF: continue
            if elev(data[i][j]) > elev(data[nI][nJ]) + 1: continue
            q.append([nI,nJ])
            dist[nI][nJ] = dist[i][j] + 1
            if data[nI][nJ] == 'E':
                ans = dist[nI][nJ]
                break
    print(ans)

# Part 2
def p2():
    n, m, INF = len(data), len(data[0]), 100000000
    dist = [[INF for i in range(m)] for i in range(n)]
    q = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'S' or data[i][j] == 'a':
                q.append([i,j])
                dist[i][j] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    def inside(i, j):
        return i<n and j<m and i>=0 and j>=0

    ans = 0
    while q:
        i, j = q.pop(0)
        for k in range(4):
            nI, nJ = i + dx[k], j + dy[k]
            if not inside(nI, nJ): continue 
            # print(nI,nJ)
            if dist[nI][nJ] != INF: continue
            if elev(data[i][j]) > elev(data[nI][nJ]) + 1: continue
            q.append([nI,nJ])
            dist[nI][nJ] = dist[i][j] + 1
            if data[nI][nJ] == 'E':
                ans = dist[nI][nJ]
                break
    print(ans)

p1()
p2()