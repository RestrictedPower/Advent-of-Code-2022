#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read()

moves = [
    [[0,0],[0,1],[0,2],[0,3]],
    [[1,0],[0,1],[1,1],[2,1],[1,2]],
    [[0,0],[0,1],[0,2],[1,2],[2,2]],
    [[0,0],[1,0],[2,0],[3,0]],
    [[0,0],[0,1],[1,0],[1,1]]
]

def shiftSet(current, dHeight, dWidth):
    s = []
    for i in current:
        s.append([i[0]+dHeight,i[1]+dWidth])
    return s

def solve(BLOCK_GOAL):
    blocked = set((0,i) for i in range(7))
    currentMaxHeight =  0
    currentSet = shiftSet(moves[0], 4, 2)
    moveIndex = 0
    blocksFallen = 0
    extraHeight = 0

    def isInValidPosition(currentSet):
        for i in currentSet:
            if tuple([i[0],i[1]]) in blocked:
                return False
            if not (0 <= i[1] and i[1] < 7):
                return False
        return True

    def hash():
        xs = set()
        for i in blocked:
            if currentMaxHeight - i[0] <= 20:
                xs.add((currentMaxHeight - i[0], i[1]))
        return (blocksFallen%5, frozenset(xs))

    calc = {}

    while True:
        # Shift first
        shifted = None
        if data[moveIndex] == '>':
            shifted = shiftSet(currentSet, 0, 1)
        else:
            shifted = shiftSet(currentSet, 0, -1)

        if isInValidPosition(shifted):
            currentSet = shifted

        moveIndex = (moveIndex + 1) % len(data)

        # Move down next
        movedDown = shiftSet(currentSet, -1, 0)
        if isInValidPosition(movedDown):
            currentSet = movedDown
            continue
        
        # Can't go down, place here.
        for i in currentSet:
            blocked.add(tuple([i[0],i[1]]))
            currentMaxHeight = max(currentMaxHeight, i[0])
        blocksFallen += 1

        hs = hash()
        if hs in calc and extraHeight == 0:
            blocksFallenOld, maxHeightOld = calc[hs]
            hD = currentMaxHeight - maxHeightOld
            blocksD = blocksFallen - blocksFallenOld
            fit = (BLOCK_GOAL - blocksFallen) // blocksD
            extraHeight = fit * hD
            blocksFallen += fit * blocksD

        calc[hs] = [blocksFallen, currentMaxHeight]

        currentSet = shiftSet(moves[blocksFallen%5], 4 + currentMaxHeight, 2)
        if blocksFallen == BLOCK_GOAL:
            break
    return (currentMaxHeight + extraHeight)

print(solve(2022))
print(solve(1000000000000))