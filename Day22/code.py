#!/usr/bin/env python3
from collections import defaultdict

inputName = 'input.txt'
inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

moveX = [[-1,-1,-1], [1,1,1], [0,-1,1], [0,-1,1]]
moveY = [[0,-1,1], [0,-1,1], [-1,-1,-1], [1,1,1]]

def dbg(state):
    mnX = min(state, key=lambda i : i[0])[0]
    mxX = max(state, key=lambda i : i[0])[0]

    mnY = min(state, key=lambda i : i[1])[1]
    mxY = max(state, key=lambda i : i[1])[1]
    for i in range(mnX, mxX+1):
        st = ""
        for j in range(mnY, mxY+1):
            if (i,j) in state:
                st += "#"
            else:
                st += "."
        print(st)
    print()

# Part 1
state = set([(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == '#'])

for idx in range(1):
    X, Y = moveX[idx%4], moveY[idx%4]
    posFreq = defaultdict(lambda: 0)
    moveMap = {}
    for i in state:
        posClear = True
        for j in range(3):
            if (i[0] + X[j], i[1] + Y[j]) in state:
                posClear = False
        if posClear:
            pos = (i[0] + X[0], i[1] + Y[0])
            moveMap[i] = pos
            posFreq[pos] += 1
    dbg(state)
    nextState = set()
    for i in state:
        if i in moveMap and posFreq[moveMap[i]] == 1:
            nextState.add(moveMap[i])
        else:
            nextState.add(i)
    state = nextState

dbg(state)
mnX = min(state, key=lambda i : i[0])[0]
mxX = max(state, key=lambda i : i[0])[0]

mnY = min(state, key=lambda i : i[1])[1]
mxY = max(state, key=lambda i : i[1])[1]

print(mnX, mxX, mnY, mxY)
    #     # print(i)
    # exit()

