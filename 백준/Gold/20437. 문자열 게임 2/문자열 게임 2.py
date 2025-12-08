def solve(W, K):
    # 각 문자의 위치를 저장
    char_positions = {}
    for i, char in enumerate(W):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)

    min_length = float('inf')
    max_length = 0
    found = False

    # 각 문자에 대해 K개씩 묶어서 확인
    for char in char_positions:
        positions = char_positions[char]
        # K개 미만이면 불가능
        if len(positions) < K:
            continue

        found = True
        # i번째부터 (i+K-1)번째까지가 K개를 포함하는 부분 문자열
        for i in range(len(positions) - K + 1):
            start = positions[i]
            end = positions[i + K - 1]
            length = end - start + 1

            # 3번 조건: 최소 길이
            min_length = min(min_length, length)
            # 4번 조건: 자동으로 같은 문자로 시작/끝
            max_length = max(max_length, length)

    if not found:
        return -1, -1

    return min_length, max_length


T = int(input())
for _ in range(T):
    W = input()
    K = int(input())

    if K == 1:
        print("1 1")
        continue

    min_len, max_len = solve(W, K)

    if min_len == -1:
        print(-1)
    else:
        print(min_len, max_len)