word = str(input())

word_list = list(word)
reversed_word = list(reversed(word_list))

A, B = [], []

for i in word_list:
    A.append(i)
for i in reversed_word:
    B.append(i)

if A == B:
    print("1")
else:
    print("0")