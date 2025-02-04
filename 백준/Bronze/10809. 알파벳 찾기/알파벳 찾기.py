S = str(input())

S_list = list(map(str, str(S)))

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet_list)):
    if alphabet_list[i] in S_list:
        print(S_list.index(alphabet_list[i]), end = " ")
    else:
        print("-1", end = " ")