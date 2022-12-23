#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 2
n = len(data)
sensors = []
closestBeacon = {}
beacons = []

fixedY = 2000000
mx = 4000000

if 'test' in inputName:
    fixedY = 10
    mx = 20

def dist(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

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

def isDes(A):
    if A[0] < 0 or A[1] < 0 or mx < A[0] or mx < A[1]: return False
    for sen in sensors:
        cap = dist(sen, closestBeacon[sen])
        if dist(sen, A) <= cap:
            return False
    return True

for i in sensors:
    # Assumtion: it must be covered by an edge of some sensor manhattan square.
    estimatedDistance = dist(i, closestBeacon[i]) + 1
    x, y = i[0]-estimatedDistance, i[1] 
    for i in range(estimatedDistance):
        if isDes((x+i,y+i)):
            print((x+i)*4000000 + y+i)
            exit()