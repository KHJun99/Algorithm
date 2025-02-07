T = int(input())

for i in range(T):
    Repeat, S = input().split()
    Repeat = int(Repeat)

    S_list = list(map(str, str(S)))
    for j in range(len(S_list)):
        print(S_list[j] * Repeat, end = "")
    print("")