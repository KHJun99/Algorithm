word = []

# 5개의 문자열 입력
for i in range(5):
    current_input = list(input())
    word.append(current_input)

# 가장 긴 문자열의 길이
max_length = max(len(w) for w in word)

# 각 문자열의 길이를 맞춤
for i in range(len(word)):
    while len(word[i]) < max_length:
        word[i].append(' ')  # 공백 추가

# 세로로 출력
for i in range(max_length):
    for j in range(len(word)):
        # 공백이 아닐 경우에만 출력
        if word[j][i] != ' ':
            print(word[j][i], end="")