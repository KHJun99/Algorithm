# 문자열 반복
T = int(input())
for tc in range(T):
    r, word = input().split()

    r_word = []
    for i in range(len(word)):
        r_word.append(word[i] * int(r))

    print(*r_word, sep='')