def check(length, star_lst):
    global result

    for i in range(K):
        for j in range(K):
            tx = star_lst[i][0]
            ty = star_lst[j][1]

            count = 0
            for sx, sy in star_lst:
                if tx <= sx <= tx + length and ty <= sy <= ty + length:
                    count += 1

            result = max(result, count)


""" 변수 설명
N : 별똥별이 떨어지는 구역의 가로 길이
M : 별똥별`이 떨어지는 구역의 세로 길이
L : 트램펄린의 한 변의 길이
K : 별똥별의 수
"""
N, M, L, K = map(int, input().split())
starts = [list(map(int, input().split())) for _ in range(K)]

result = 0

check(L, starts)

print(K - result)