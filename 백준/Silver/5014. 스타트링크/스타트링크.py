from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque()
queue.append((S, 0))

floors = [False] * (F + 1)

is_goal = False
while queue:
    floor, cnt = queue.popleft()

    if floor == G:
        is_goal = True
        break
    
    floors[floor] = True

    if floor + U <= F and not floors[floor + U]:
        floors[floor + U] = True
        queue.append((floor + U, cnt + 1))

    if floor - D >= 1 and not floors[floor - D]:
        floors[floor - D] = True
        queue.append((floor - D, cnt + 1))
    

if is_goal:
    print(cnt)
else:
    print("use the stairs")