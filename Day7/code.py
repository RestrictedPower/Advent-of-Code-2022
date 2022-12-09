#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

sz = {}
s = []
for line in data:
    if line.startswith('$ ls') or line.startswith('dir'): continue
    if line.startswith('$ cd'):
        node = line.split(' ')[-1]
        if node == '..':
            cur = '/'.join(s)
            s.pop()
            if len(s) != 0:
                sz['/'.join(s)] += sz[cur]
        else:
            s.append(node)
            if '/'.join(s) not in sz:
                sz['/'.join(s)] = 0
        continue

    # File case
    size, fileName = line.split()
    sz[fileName+'_FILE'] = int(size)
    sz['/'.join(s)] += int(size)

while len(s) != 0:
    cur = '/'.join(s)
    s.pop()
    if len(s) != 0:
        sz['/'.join(s)] += sz[cur]

# Part 1
ans = 0
for k, v in sz.items():
    if v <= 100000 and not k.endswith('_FILE'):
        ans += v
print(ans)

# Part 2
ans = 1e9
need = 30000000 - (70000000 - sz['/'])
for k, v in sz.items():
    if v >= need and not k.endswith('_FILE'):
        ans = min(ans, v)
print(ans)