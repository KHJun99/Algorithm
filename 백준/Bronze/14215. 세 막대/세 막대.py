num = sorted(list(map(int, input().split())))

if num[2] >= num[0] + num[1]:
    print(2 * (num[0] + num[1]) - 1)
else:
    print(sum(num))