T = int(input())
S = []

for i in range(T):
    S = str(input())

    first_element = S[0]
    last_element = S[-1]

    print(first_element, last_element, sep = "")