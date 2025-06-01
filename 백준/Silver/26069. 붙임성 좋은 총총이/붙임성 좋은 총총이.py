# 붙인성 좋은 총총이
import sys

# 빠른 입출력
input = sys.stdin.readline

# 만남의 수 N 입력
N = int(input())

# 춤추는 사람들 set (처음엔 총총이만)
dancing_people = {"ChongChong"}

# N번의 만남 처리
for _ in range(N):
    # 만난 두 사람 이름 입력
    person1, person2 = input().split()

    # 둘 중 한 명이라도 춤추고 있다면
    if person1 in dancing_people or person2 in dancing_people:
        # 만난 두 사람 모두 set에 추가
        dancing_people.add(person1)
        dancing_people.add(person2)

# 최종 춤추는 사람 수 출력
print(len(dancing_people))

