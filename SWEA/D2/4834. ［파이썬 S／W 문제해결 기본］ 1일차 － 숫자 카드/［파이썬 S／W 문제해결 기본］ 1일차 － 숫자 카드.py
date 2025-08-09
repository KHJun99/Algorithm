def my_max(lst):
    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]

    return max_value

# def my_count(lst, num):
#     count = 0
#     for i in range(len(lst)):
#         if lst[i] == num:
#             count += 1
#     return count

def counting_card(lst, k):
    count = [0] * (k + 1)
    temp = [0] * len(lst)

    for i in range(len(lst)):
        count[lst[i]] += 1

    # for i in range(1, len(count)):
    #     count[i] += count[i-1]
    #
    # for i in range(len(lst) - 1, -1, -1):
    #     count[lst[i]] -= 1
    #     temp[count[lst[i]]] = lst[i]

    max_count = my_max(count)
    for j in range(len(count) - 1, -1, -1):
        if count[j] == max_count:
            return f'{j} {max_count}'
    return None

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    card_lst = list(map(int, input()))
    max_val = my_max(card_lst)
    result = counting_card(card_lst, max_val)
    print(f'#{i} {result}')