A = int(input())
B = int(input())
C = int(input())

total = A * B * C

nums = []
while True:
    tmp = total % 10
    nums.append(tmp)

    total //= 10

    if total == 0:
        break

for i in range(10):
    print(nums.count(i))