import sys

n = int(sys.stdin.readline().strip())
X, Y = [], []

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    X.append(x)
    Y.append(y)

width = max(X) - min(X)
height = max(Y) - min(Y)

if n == 1:
    print('0')
else:
    print(width * height)
