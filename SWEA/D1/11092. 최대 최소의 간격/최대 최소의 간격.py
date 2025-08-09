def between_max_min(lst):
    max_value = lst[0]
    min_value = lst[0]
    max_idx = 0
    min_idx = 0
    for i in range(len(lst) -1 , -1, -1):
        if lst[i] > max_value:
            max_value = lst[i]
            max_idx = i

    for i in range(len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_idx = i

    between = abs(max_idx - min_idx)
    return between

# T : 테스트 케이스
# N : 양수의 개수
# arr : N개의 양수

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = between_max_min(arr)
    print(f'#{i} {result}')