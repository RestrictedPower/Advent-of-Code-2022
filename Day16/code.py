#!/usr/bin/env python3

inputName = 'input.txt'
inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

adj = {}
cost = {}
x = 0
for line in data:
    currentNode = line.split(' ')[1]
    rate = int(line.split(';')[0].split('=')[1])
    cost[currentNode] = rate
    adj[currentNode] = []
    for to in line.replace('valves','valve').split('valve')[1].strip().split(', '):
        adj[currentNode].append(to)

def dfs(i, taken, time, haveOther):
    if time < 0: return -10000
    if time == 0 and not haveOther: return 0
    s = (i, frozenset(taken), time, haveOther)
    if s in memo: 
        return memo[s]
    if time == 0: # First finished, initialize second.
        return dfs('AA', taken, 26, False)
    ans = 0
    for j in adj[i]:
        if cost[j] > 0 and not j in taken:
            taken.add(j)
            ans = max(ans, dfs(j, taken, time-2, haveOther) + (time-2) * cost[j])
            taken.remove(j)
        ans = max(ans, dfs(j, taken, time-1, haveOther))
    memo[s] = ans
    return ans

# Part 1
memo = {}
print(dfs('AA', set(), 30, False))

# Part 2
memo = {}
print(dfs('AA', set(), 26, True))

