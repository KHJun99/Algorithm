import sys

input = sys.stdin.readline

n = int(input())
card1 = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

# card1의 숫자별 등장 횟수를 딕셔너리에 저장
count_dict = {}
for num in card1:
    count_dict[num] = count_dict.get(num, 0) + 1

# card2의 각 숫자에 대해 등장 횟수 출력 (없으면 0)
for num in card2:
    print(count_dict.get(num, 0), end=' ')
