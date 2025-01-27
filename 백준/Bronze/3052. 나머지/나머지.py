Number = []
Share = []
Count = 0

for i in range(10):
    Num = int(input())
    Number.append(Num)

for i in range(len(Number)):
    Share.append(Number[i] % 42)

# Share 리스트에서 중복된 나머지를 제거하여 Count 계산
Count = len(set(Share))

print(Count)
