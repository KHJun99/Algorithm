def time():
    result = [schedule[0]]
    i = 0
    j = 1
    while j != len(schedule):
        if result[i][1] <= schedule[j][0]:
            result.append(schedule[j])
            i += 1
            j += 1
        else:
            j += 1
    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        schedule.append((s, e))

    # 종료 시간 기준 정렬
    schedule.sort(key=lambda x:x[1])

    result = time()
    print(f'#{tc} {len(result)}')
