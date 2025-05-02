import sys
import math

input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해 표준 입력을 빠르게 읽는 방식 사용

def isprime(num):
    # 주어진 수가 소수인지 판별하는 함수. 소수면 True, 아니면 False 반환
    if num < 2:              # 2보다 작은 수는 소수가 아님
        return False
    if num == 2:             # 2는 유일한 짝수 소수
        return True
    if num % 2 == 0:         # 2를 제외한 짝수는 모두 소수가 아님
        return False
    # 3부터 √num까지 홀수만 검사
    for i in range(3, int(math.isqrt(num)) + 1, 2):
        if num % i == 0:     # 나눠지는 수가 있으면 소수가 아님
            return False
    return True              # 위 조건을 모두 통과하면 소수

num = int(input())           # 테스트 케이스 개수 입력

for _ in range(num):
    test = int(input())      # 테스트 숫자 입력
    while True:
        if isprime(test):    # 현재 수가 소수면 출력 후 종료
            print(test)
            break
        test += 1            # 소수가 아니면 다음 수를 검사
