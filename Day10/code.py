#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

# Part 1
ans, x, cyc = 0, 1, 0

def inc():
    global x, cyc, ans
    cyc += 1
    if (cyc-20) % 40 == 0:
        ans += x*(cyc)

for line in data:
    if line[0] == 'n':
        inc()
        continue
    inc()
    inc()
    x += int(line.split(' ')[1])

print(ans)

# Part 2
x, cyc = 1, 0
H, W = 6, 40
ans = ['.' for i in range(H*W)]

def inc2():
    global x, cyc
    if cyc % 40 == x-1 or cyc % 40 == x or cyc % 40 == x+1:
        ans[cyc] = '#'
    cyc += 1

for line in data:
    if line[0] == 'n':
        inc2()
        continue
    inc2()
    inc2()
    x += int(line.split(' ')[1])

for i in range(H):
    print("".join(ans[i*W:(i+1)*W-1]))