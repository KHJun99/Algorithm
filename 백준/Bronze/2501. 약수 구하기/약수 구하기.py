N, K = map(int, input().split())

result = []

# 약수를 찾는 과정
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        result.append(i)  # i를 약수로 추가
        if i != N // i:   # N // i도 약수일 경우 추가
            result.append(N // i)

# 약수들을 정렬
result.sort()

# K번째 약수 출력
if len(result) >= K:
    print(result[K-1])
else:
    print('0')
