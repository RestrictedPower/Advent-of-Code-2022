#!/usr/bin/env python3

inputName = 'input.txt'
# inputName = 'test.txt'

inputFile = open(inputName, 'r')
data = inputFile.read().split('\n')

dirX = {'U':1, 'D':-1,'L':0,'R':0}
dirY = {'U':0, 'D':0,'L':-1,'R':1}
def hash(x, y):
    return str(x)+':'+str(y)

# Part 1
hX, hY = 0,0
tX, tY = 0,0

s = set()

s.add(hash(tX,tY))

for line in data:
    dir = line.split(' ')[0]
    amount = int(line.split(' ')[1])

    for x in range(amount):
        hX += dirX[dir]
        hY += dirY[dir]
        if ((abs(hX-tX)==0 or abs(hY-tY)==0) and abs(hX-tX) + abs(hY-tY) >= 2) or abs(hX-tX) + abs(hY-tY) > 2:
            if hX > tX:
                tX += 1
            elif hX<tX:
                tX -= 1
            if hY > tY:
                tY += 1
            elif hY < tY:
                tY -= 1
            s.add(hash(tX,tY))
print(len(s))



# Part 2
X = [0 for i in range(10)]
Y = [0 for i in range(10)]
s = set()
s.add(hash(0,0))

for line in data:
    dir = line.split(' ')[0]
    amount = int(line.split(' ')[1])
    for x in range(amount):
        X[9] += dirX[dir]
        Y[9] += dirY[dir]
        for i in reversed(range(9)):
            if ((abs(X[i+1]-X[i])==0 or abs(Y[i+1]-Y[i])==0) and abs(X[i+1]-X[i]) + abs(Y[i+1]-Y[i]) >= 2) or abs(X[i+1]-X[i]) + abs(Y[i+1]-Y[i]) > 2:
                if X[i+1] > X[i]:
                    X[i] += 1
                elif X[i+1] < X[i]:
                    X[i] -= 1

                if Y[i+1] > Y[i]:
                    Y[i] += 1
                elif Y[i+1] < Y[i]:
                    Y[i] -= 1

                if(i == 0):
                    s.add(hash(X[i],Y[i]))
print(len(s))
