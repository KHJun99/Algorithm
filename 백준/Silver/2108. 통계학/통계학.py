import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

# 입력이 0개 아니면 계산 시작!
if n > 0:
    # 정렬 (중앙값, 범위 계산용)
    num_sorted = sorted(num)

    # 1. 산술평균
    # 총합 / 개수 후 반올림해서 정수!
    avg = sum(num) / n
    print(int(round(avg)))

    # 2. 중앙값
    # 정렬된 가운데 값!
    print(num_sorted[n // 2])

    # 3. 최빈값
    counter = Counter(num) # 숫자별 개수 카운트!
    # (값, 빈도수) 튜플 리스트 (빈도 높은 순, 값 오름차순 정렬됨!)
    most_common_items = counter.most_common()
    max_freq = most_common_items[0][1] # 가장 높은 빈도수!

    modes_at_max_freq = [] # 가장 높은 빈도수를 가진 값들 모을 리스트
    # most_common_items 돌면서 max_freq랑 빈도수 같은 값들만 담기
    for item, freq in most_common_items:
        if freq == max_freq:
            modes_at_max_freq.append(item)
        else:
            break # 빈도수 작아지면 멈춰!

    # *** 수정된 부분 시작 ***
    # 혹시 모를 most_common()의 빈도수 같을 때 정렬 문제를 대비해서
    # 최빈값 후보 리스트를 값 오름차순으로 한 번 더 정렬!
    modes_at_max_freq.sort()
    # *** 수정된 부분 끝 ***

    # 최빈값이 여러 개면 (리스트 길이가 1보다 크면) 두 번째로 작은 값 출력!
    # modes_at_max_freq가 값 오름차순으로 정렬됐으니 [1] 인덱스가 두 번째 작은 값이야.
    if len(modes_at_max_freq) > 1:
        print(modes_at_max_freq[1])
    else:
        # 최빈값이 하나뿐이면 그 값 출력!
        print(modes_at_max_freq[0])

    # 4. 범위
    # 정렬된 리스트의 최대값 - 최소값!
    data_range = num_sorted[-1] - num_sorted[0]
    print(data_range)

