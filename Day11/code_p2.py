#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n\n')

# Part 2
n = len(data)
monkeyInfo = {}
inspections = {}
div = 1
for i in range(n):
    monkeyInfo[i] = {}
    inspections[i] = 0
    d = data[i].split('\n')
    monkeyInfo[i]['stack'] = d[1].split(":")[1].strip().split(", ")
    monkeyInfo[i]['op'] = d[2].split('=')[1].strip().replace('old','x')
    monkeyInfo[i]['div'] = int(d[3].split('by')[1].strip())
    monkeyInfo[i]['true'] = int(d[4].split('monkey')[1].strip())
    monkeyInfo[i]['false'] = int(d[5].split('monkey')[1].strip())
    div *= monkeyInfo[i]['div']

# Part 1
for _ in range(10000):
    for i in range(n):
        while monkeyInfo[i]['stack']:
            inspections[i] += 1
            v = int(monkeyInfo[i]['stack'].pop(0))
            result = (eval(monkeyInfo[i]['op'].replace('x',str(v))) % div)
            if result % monkeyInfo[i]['div'] == 0:
                monkeyInfo[monkeyInfo[i]['true']]['stack'].append(result)
            else:
                monkeyInfo[monkeyInfo[i]['false']]['stack'].append(result)

a = sorted(inspections.values())
print(a[-1]*a[-2])