result = []

while True:
    try:
        A, B = map(int, input().split())
        result.append(A + B)
    except (EOFError, ValueError):
        break

for num in result:
    print(num)