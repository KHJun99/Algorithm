X, Y = [], []

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x = X[0] ^ X[1] ^ X[2]
y = Y[0] ^ Y[1] ^ Y[2]
print(x, y)

