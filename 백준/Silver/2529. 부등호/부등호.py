def check(a, b, sign):
    if sign == '<':
        return a < b
    else:
        return a > b


def make_num(depth, num_str):
    if depth == k + 1:
        results.append(num_str)
        return

    for num in range(10):
        if visited[num]:
            continue

        if depth > 0:
            prev_num = int(num_str[-1])
            curr_sign = signs[depth - 1]

            if not check(prev_num, num, curr_sign):
                continue

        visited[num] = True
        make_num(depth + 1, num_str + str(num))
        visited[num] = False

k = int(input())
signs = input().split()
visited = [False] * 10
results = []

make_num(0, "")

# results.sort()

print(results[-1])
print(results[0])