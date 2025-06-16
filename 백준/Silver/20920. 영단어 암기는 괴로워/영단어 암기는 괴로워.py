import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

words = [input().strip() for _ in range(n)]

# 길이가 m 이상인 단어만 필터링
filtered_words = [word for word in words if len(word) >= m]

# 등장 횟수 세기
counts = Counter(filtered_words)

# 정렬 기준: (-빈도, -길이, 사전순)
sorted_words = sorted(counts.keys(), key=lambda x: (-counts[x], -len(x), x))

# 출력
for word in sorted_words:
    print(word)
