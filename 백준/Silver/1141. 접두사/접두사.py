N = int(input())

words = set()
for _ in range(N):
    word = input().strip()
    words.add(word)

sorted_words = sorted(list(words), key=lambda x: len(x))
M = len(sorted_words)

remove = set()
for idx1 in range(M):
    for idx2 in range(idx1 + 1, M):
        word, length = sorted_words[idx1], len(sorted_words[idx1])

        if sorted_words[idx2][0:length] == word:
            remove.add(word)

result = [w for w in sorted_words if w not in remove]

print(len(result))