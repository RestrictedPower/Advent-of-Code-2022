#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
n = len(data)
sensors = []
closestBeacon = {}
beacons = []

fixedY = 2000000

if 'test' in inputName:
    fixedY = 10

def dist(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

mn, mx = int(1e9), int(-1e9)
mxDist = 0
for line in data:
    x = line.split(':')[0]
    y = line.split(':')[1]
    A = (int(x.split('=')[1].split(',')[0].strip()), int(x.split('=')[2].strip()))
    B = (int(y.split(',')[0].split('=')[1].strip()), int(y.split(',')[1].split('=')[1].strip()))
    mxDist = max(mxDist, dist(A,B))
    sensors.append(A)
    closestBeacon[A] = B
    beacons.append(B)

ans = 0
visitedPositions = set()
for sen in sensors:
    cap = dist(sen, closestBeacon[sen])

    p = (sen[0], fixedY)
    while dist(sen, p) <= cap:
        if p not in visitedPositions and p not in beacons:
            visitedPositions.add(p)
            ans += 1
        p = (p[0] + 1, fixedY)

    p = (sen[0] - 1, fixedY)
    while dist(sen, p) <= cap:
        if p not in visitedPositions and p not in beacons:
            visitedPositions.add(p)
            ans += 1
        p = (p[0] - 1, fixedY)

print(ans)