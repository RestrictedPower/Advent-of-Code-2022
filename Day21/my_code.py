#!/usr/bin/env python3
import sympy as sp
from sympy import symbols, solve

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')


adj = {}
numMap = {}

for line in data:
    u = line.split(':')[0]
    args = line.split(' ')
    if len(args) < 3:
        numMap[u] = int(args[1].strip())
        continue
    u1, u2, op = args[1], args[3], args[2]
    adj[u] = (u1,u2,op)

# Part 1
def dfs(i):
    if i in numMap:
        return numMap[i]
    u1, u2, op = adj[i][0], adj[i][1], adj[i][2]
    return eval(str(dfs(u1)) + op + str(dfs(u2)))

print(dfs('root'))

# Part 2
numMap['humn'] = 'x'

def dfs2(i):
    if i in numMap:
        return numMap[i]
    u1, u2, op = adj[i][0], adj[i][1], adj[i][2]
    if i == 'root':
        l, r = str(dfs2(u1)), str(dfs2(u2))
        return l + '-' + r + ' = 0'
    return '('+(str(dfs2(u1)) + op + str(dfs2(u2)))+')'

eq = dfs2('root')
sympy_eq = sp.sympify("Eq(" + eq.replace("=", ",") + "0)")
print(solve(sympy_eq))
