#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

n = 0
start = 0
stackMap = {}

def parse():
    global n, start, stackMap
    stackMap = {}
    for i in range(len(data)):
        if(len(data[i])==0):
            n = int(data[i-1].strip().split('  ')[-1].strip())
            for j in range(1, n+1):
                stackMap[j] = []
            for idx in reversed(range(0, i-1)):
                curLine = data[idx]
                charIdx = 1
                for j in range(n):
                    c = curLine[charIdx]
                    charIdx += 4
                    if c != ' ':
                        stackMap[j+1].append(c)
            start = i+1
            break

# Part 1
parse()
for lineIdx in range(start, len(data)):
    line = data[lineIdx]
    amount, _from, _to = map(int, line.split(' ')[1:6:2])
    for i in range(amount):
        stackMap[_to].append(stackMap[_from].pop())

ans = "".join([stackMap[i][-1] for i in range(1, n+1)])
print(ans)

# Part 2
parse()
for lineIdx in range(start, len(data)):
    line = data[lineIdx]
    amount, _from, _to = map(int, line.split(' ')[1:6:2])
    for i in range(len(stackMap[_from])-amount,len(stackMap[_from])):
        stackMap[_to].append(stackMap[_from][i])
    stackMap[_from] = stackMap[_from][:len(stackMap[_from])-amount]

ans = "".join([stackMap[i][-1] for i in range(1, n+1)])
print(ans)
