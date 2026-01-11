from collections import deque

# 1단계 : 회전 함수
def rotation(n):
    durability.rotate(1)
    robot_lst.rotate(1)

    # 회전 후 내리는 위치에 로봇이 있으면 바로 내림
    if robot_lst[n - 1]:
        robot_lst[n - 1] = False

# 2단계 : 로봇 이동 함수
def moving_robot(n):
    global robot_lst, durability

    for i in range(n - 2, -1, -1):
        # 현재 칸에 로봇 존재 + 다음 칸 empty + 다음 칸 내구도 1 이상
        if robot_lst[i] and not robot_lst[i + 1] and durability[i + 1] >= 1:
            robot_lst[i] = False
            robot_lst[i + 1] = True
            durability[i + 1] -= 1

    # 이동 후 내리는 위치 체크
    if robot_lst[n - 1]:
        robot_lst[n - 1] = False

# 3단계 : 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇을 올린다.
def putting_robot():
    global robot_lst, durability

    if durability[0] >= 1:
        robot_lst[0] = True
        durability[0] -= 1

# 4단계 : 내구도가 0인 칸의 개수가 K개 이상이라면 종료
def termination_condition(k):
    return durability.count(0) < k

N, K = map(int, input().split())
durability = deque(map(int, input().split()))
robot_lst = deque([False] * 2 * N)

step = 0
while termination_condition(K):
    step += 1
    rotation(N)
    moving_robot(N)
    putting_robot()

print(step)