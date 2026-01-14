def make_snowball(size, time, idx):
    global max_size

    if time == M or idx == N:
        max_size = max(max_size, size)
        return

    if idx + 1 <= N:
        make_snowball(size + array[idx + 1], time + 1, idx + 1)

    if idx + 2 <= N:
        make_snowball((size // 2) + array[idx + 2], time + 1, idx + 2)


# 1 <= N <= 100, 1 <= M <= 10
# N : 앞마당의 길이, M : 대회의 시간
N, M = map(int, input().split())
array = [0] + list(map(int, input().split()))

snowball_size = 1
max_size = float('-inf')

make_snowball(snowball_size, 0, 0)

print(max_size)