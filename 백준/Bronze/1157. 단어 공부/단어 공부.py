word = input().lower()              # word = [mississipi]
word_list = list(set(word))         # word_list = ['m', 'i', 's', 'p']
cnt = []

for i in word_list:                 # i = m, i, s, p
    count = word.count(i)
    cnt.append(count)               # cnt = [4, 4, 1, 1]

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())