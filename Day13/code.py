#!/usr/bin/env python3
import json, functools

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n\n')

def cmp(A, B):
    if type(A) != type(B):
        if type(A) == int:
            A = [A]
        if type(B) == int:
            B = [B]
    if type(A) == int:
        if A < B: return -1
        if A > B: return 1
        return 0
    for i in range(max(len(A),len(B))):
        if i >= len(A): return -1
        if i >= len(B): return 1
        comp = cmp(A[i], B[i])
        if comp != 0: return comp
    return 0

# Part 1
ans, idx = 0, 1
for segment in data:
    f, s = map(json.loads, segment.split())
    if cmp(f,s) < 0: ans += idx
    idx += 1
print(ans)

# Part 2
all = []
ans, idx = 0, 1
for segment in data:
    f, s = map(json.loads, segment.split())
    all.append(f)
    all.append(s)
all.append([[2]])
all.append([[6]])
all.sort(key=functools.cmp_to_key(cmp))
f, s, idx = 0,0,1
for i in all:
    if i == [[2]]:
        f = idx
    if i == [[6]]:
        s = idx
    idx += 1
print(f*s)