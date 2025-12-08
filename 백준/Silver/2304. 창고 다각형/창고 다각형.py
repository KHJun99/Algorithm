N = int(input())
storage = [list(map(int, input().split())) for _ in range(N)]

storage.sort()

max_height = 0
max_height_idx = 0

for i in range(N):
    if max_height < storage[i][1]:
        max_height = storage[i][1]
        max_height_idx = i

extent = max_height  # 최대 높이 기둥의 넓이 (폭 1 * 높이)

# 왼쪽에서 최대 높이 직전까지
start_height = storage[0][1]
for i in range(1, max_height_idx + 1):
    extent += (storage[i][0] - storage[i - 1][0]) * start_height
    if storage[i][1] > start_height:
        start_height = storage[i][1]

# 오른쪽에서 최대 높이 직후부터
start_height = storage[N - 1][1]
for i in range(N - 1, max_height_idx, -1):
    extent += (storage[i][0] - storage[i - 1][0]) * start_height
    if storage[i - 1][1] > start_height:
        start_height = storage[i - 1][1]

print(extent)