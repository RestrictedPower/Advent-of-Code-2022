#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
stones = set()

for line in data:
    args = list(list(map(int, item.split(','))) for item in line.split(' -> '))
    for i in range(len(args)-1):
        x, y = args[i]
        xF, yF = args[i+1]
        stones.add((x,y))
        while x != xF or y != yF:
            if x > xF:
                x -= 1
            if x < xF:
                x += 1
            if y > yF:
                y -= 1
            if y < yF:
                y += 1
            stones.add((x,y))

abyssX = min(stones, key = lambda x: x[0])[0]

sand = set()
ans = 0
while True:
    sand.add((500, 0))
    moved = True
    reachedAbyss = False
    while not reachedAbyss:
        moved = {}
        for i in sand:
            if i[0] == abyssX:
                reachedAbyss = True
                break
            below = (i[0] + 0, i[1] + 1)
            if below not in sand and below not in stones:
                while (below[0], below[1]+1) not in sand and (below[0], below[1]+1) not in stones:
                    below = (below[0], below[1]+1)
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
    if reachedAbyss:
        break
    ans += 1

print(ans)