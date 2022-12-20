#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
n = len(data)
tempList = [(i, int(data[i])) for i in range(len(data))]
for idx in range(n):
    idx = [i for i in range(n) if tempList[i][0] == idx][0]
    val = tempList.pop(idx)
    toGo = (idx + val[1])%len(tempList)
    tempList.insert(toGo, val)
    
idx = [i for i in range(n) if tempList[i][1] == 0][0]
ans = sum([tempList[(idx + i) % n][1] for i in (1000, 2000, 3000)])
print(ans)

# Part 2
n, key = len(data), 811589153
tempList = [(i, int(data[i])*key) for i in range(len(data))]
for rep in range(10):
    for idx in range(n):
        idx = [i for i in range(n) if tempList[i][0] == idx][0]
        val = tempList.pop(idx)
        toGo = (idx + val[1])%len(tempList)
        tempList.insert(toGo, val)
    
idx = [i for i in range(n) if tempList[i][1] == 0][0]
ans = sum([tempList[(idx + i) % n][1] for i in (1000, 2000, 3000)])
print(ans)