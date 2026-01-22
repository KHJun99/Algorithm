def work(index, profit):
    global max_profit
    
    # 범위를 벗어나면 종료
    if index > N:
        max_profit = max(max_profit, profit)
        return
    
    # 현재 상담을 할 수 있는 경우
    next_index = index + schedule[index][0]
    
    if next_index <= N + 1:  # ← N+1로 변경! (퇴사일까지 일할 수 있음)
        # 상담을 하는 경우
        work(next_index, profit + schedule[index][1])
    
    # 상담을 안 하는 경우 (다음 날로)
    work(index + 1, profit)


N = int(input())

schedule = [[0, 0]]
for _ in range(N):
    T, P = map(int, input().split())
    schedule.append([T, P])

max_profit = 0

work(1, 0)

print(max_profit)
