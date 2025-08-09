num_dict = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

T = int(input())

for tc in range(1, T + 1):
    case, word_len = map(str, input().split())
    word_lst = list(map(str, input().split()))

    trans_lst = []
    for word in range(int(word_len)):
        if word_lst[word] in num_dict.keys():
            trans_lst.append(num_dict[word_lst[word]])

    sorted_lst = sorted(trans_lst)

    result_lst = []
    for i in range(len(sorted_lst)):
        for key, value in num_dict.items():
            if value == sorted_lst[i]:
                result_lst.append(key)
    print(f'#{tc}')
    print(*result_lst)