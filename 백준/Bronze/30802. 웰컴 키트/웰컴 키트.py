N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt = 0

for size in sizes:
    if size % T == 0:
        shirt += size // T
    else:
        shirt += size // T + 1

pens = N // P
pen = N % P

print(shirt)
print(pens, pen)