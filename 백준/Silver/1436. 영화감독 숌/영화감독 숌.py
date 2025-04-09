n = int(input())

num = 0
series = []

while True:
    num += 1
    if '666' in str(num):
        series.append(num)

    if len(series) == n:
        break

print(series[n - 1])