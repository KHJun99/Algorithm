import sys

n = int(sys.stdin.readline())
word_set = set()  # 중복 제거를 위한 집합

for i in range(n):
    word_set.add(sys.stdin.readline().strip())  # 입력받은 문자열의 개행 문자 제거 및 집합에 추가

# 리스트로 변환 후 길이 기준으로 정렬하고, 같은 길이의 단어는 사전식으로 정렬
word = sorted(word_set, key=lambda x: (len(x), x))

# 정렬된 단어를 출력
for w in word:
    print(w)
