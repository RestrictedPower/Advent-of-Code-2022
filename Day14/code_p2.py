#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 2
stones = set()
mx = 0
for line in data:
    args = list(list(map(int, item.split(','))) for item in line.split(' -> '))
    for i in range(len(args)-1):
        x, y = args[i]
        xF, yF = args[i+1]
        stones.add((x,y))
        while x != xF or y != yF:
            mx = max(mx, y+2)
            if x > xF:
                x -= 1
            if x < xF:
                x += 1
            if y > yF:
                y -= 1
            if y < yF:
                y += 1
            stones.add((x,y))

# Ground
for i in range(-15000, 15000):
    stones.add((i, mx))

sand = set()
ans = 0
while True:
    if (500, 0) in sand: break
    
    # Optimization begin:
    # If some sand has only stone below it, it can be considered stone (we won't have to operate over it again).
    newStones = []
    for i in sand:
        onlyStoneBelow = True # Reached bottom
        for d in range(-1,2):
            nextPos = (i[0] + d, i[1] + 1)
            if nextPos not in stones:
                onlyStoneBelow = False
        if onlyStoneBelow:
            newStones.append(i)
    for i in newStones:
        sand.remove(i)
        stones.add(i)
    # Optimisation end.

    sand.add((500, 0))
    moved = True
    while True:
        moved = {}
        for i in sand:
            below = (i[0] + 0, i[1] + 1)
            if below not in sand and below not in stones:
                moved[i] = below
                continue
            
            left = (i[0] - 1, i[1] + 1)
            if left not in sand and left not in stones:
                moved[i] = left
                continue

            right = (i[0] + 1, i[1] + 1)
            if right not in sand and right not in stones:
                moved[i] = right
                continue
        if len(moved) == 0: break
        for i in moved:
            sand.remove(i)
            sand.add(moved[i])
    ans += 1

print(ans)