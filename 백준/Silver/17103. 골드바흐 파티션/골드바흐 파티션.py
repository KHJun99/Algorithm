import sys

# 입력 속도 개선
input = sys.stdin.readline

# 최대 숫자 범위 (문제 조건)
MAX_NUM = 1000000

# 에라토스테네스의 체: is_prime[i] = True면 i는 소수
is_prime = [True] * (MAX_NUM + 1)
is_prime[0] = is_prime[1] = False

# 체 실행
for p in range(2, int(MAX_NUM ** 0.5) + 1):
    if is_prime[p]:
        for i in range(p * p, MAX_NUM + 1, p):
            is_prime[i] = False

# --- is_prime으로 소수 판별 O(1) 가능! ---

# 소수 리스트 (a를 찾을 때 사용)
primes = [i for i in range(2, MAX_NUM + 1) if is_prime[i]]

# 테스트 케이스 입력
T = int(input())
test_cases = [int(input()) for _ in range(T)]

result = []
# 각 N의 골드바흐 파티션 (A + B = N, A, B 소수) 개수 세기 (순서 무관)
for N in test_cases:
    count = 0
    # 첫 번째 소수 'a' 순회 (소수 리스트 사용)
    for a in primes:
        # 중복 방지: a > N / 2 면 종료 (a <= b만 셈)
        if a > N // 2:
            break

        # 두 번째 소수 'b' 계산
        b = N - a

        # b가 2 이상이고 소수인지 확인
        if b >= 2 and is_prime[b]:
            count += 1

    result.append(count)

# 결과 출력
for res in result:
    print(res)
