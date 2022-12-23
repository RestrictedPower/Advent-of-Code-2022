#!/usr/bin/env python3
from collections import defaultdict

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

moveX = [[-1,-1,-1], [1,1,1], [0,-1,1], [0,-1,1]]
moveY = [[0,-1,1], [0,-1,1], [-1,-1,-1], [1,1,1]]

# Part 2
state = set([(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == '#'])

idx = 0
while True:
    posFreq = defaultdict(lambda: 0)
    moveMap = {}
    for i in state:
        oneInvalid = False
        for moveIdx in range(4):
            X, Y = moveX[(idx+moveIdx)%4], moveY[(idx+moveIdx)%4]
            posClear = True
            for j in range(3):
                if (i[0] + X[j], i[1] + Y[j]) in state:
                    posClear = False
            if posClear:
                pos = (i[0] + X[0], i[1] + Y[0])
                if i not in moveMap:
                    moveMap[i] = pos
                    posFreq[pos] += 1
            else:
                oneInvalid = True
        if not oneInvalid:
            posFreq[moveMap[i]] -= 1
            del moveMap[i]
    nextState = set()
    moved = False
    for i in state:
        if i in moveMap and posFreq[moveMap[i]] == 1:
            nextState.add(moveMap[i])
            moved = True
        else:
            nextState.add(i)
    idx += 1
    if not moved:
        break
    state = nextState

print(idx)
