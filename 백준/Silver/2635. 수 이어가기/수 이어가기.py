# 백준_2635_이어가기 (S5)
"""
## [문제 정리]
- 수를 만드는 규칙
    1. 첫 번째 수로 양의 정수가 주어진다.
    2. 두 번째 수는 양의 정수 중에서 하나를 선택
    3. 세 번째 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다.
        - 예 : 세 번째 수 = 첫 번째 수 - 두 번째 수
        - 예 : 네 번째 수 = 두 번째 수 - 세 번째 수
    4. 음의 저수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.

- 입력으로 첫 번째 수가 주어질 때, 이 수에서 시작하여
- 위 규칙으로 만들어지는 최대 개수의 수를 구하는 프로그램 작성
"""
def make_num(start):
    max_seq = []

    for idx in range(start, 0, -1):
        seq = [start, idx]

        while True:
            next_num = seq[-2] - seq[-1]

            if next_num < 0:
                break

            seq.append(next_num)

        if len(seq) > len(max_seq):
            max_seq = seq

    return max_seq

num = int(input())

result = make_num(num)

print(len(result))
print(*result)