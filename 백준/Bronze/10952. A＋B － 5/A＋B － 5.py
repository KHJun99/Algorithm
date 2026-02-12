result = []

while True:
    A, B = map(int, input().split())

    if A != 0 and B != 0:
        result.append(A + B)
    else:
        break

for num in result:
    print(num)