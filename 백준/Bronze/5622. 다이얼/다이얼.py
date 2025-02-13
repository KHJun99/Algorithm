time = [3, 4, 5, 6, 7, 8, 9, 10]
dial = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"],
        ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"],
        ["T", "U", "V"], ["W", "X", "Y", "Z"]]

total_time = 0

word = str(input())
word_list = list(word)

for i in range(len(word_list)):
        for j in range(len(dial)):
                if word_list[i] in dial[j]:
                        total_time += time[j]

print(total_time)