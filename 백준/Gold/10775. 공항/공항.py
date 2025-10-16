def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

parent = list(range(G + 1))     # 초기화

ap = 0

for _ in range(P):
    gi = int(input())
    gate = find(gi)

    if gate == 0:
        break

    parent[gate] = find(gate - 1)

    ap += 1

print(ap)