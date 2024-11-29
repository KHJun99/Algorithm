total_amount = int(input())
kind = int(input())

total = 0

for _ in range(kind):
    price, count = map(int, input().split())
    total += (price * count)

if total == total_amount:
    print('Yes')
else:
    print('No')