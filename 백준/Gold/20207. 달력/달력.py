N = int(input())

day = [list(map(int, input().split())) for _ in range(N)]

last_day = max(e for s, e in day)
calendar = [0] * (last_day + 1)

for s, e in day:
    for i in range(s, e + 1):
        calendar[i] += 1

extent = 0
width = 0
height = 1

idx = 0
# 달력 순회하며 넓이 계산
for i in range(1, last_day + 1):
    if calendar[i] != 0:
        width += 1
        height = max(height, calendar[i])
    else:
        if width > 0:  # 이전에 일정이 있었다면
            extent += width * height
        width = 0
        height = 0

# 마지막 구간 처리
if width > 0:
    extent += width * height

print(extent)
