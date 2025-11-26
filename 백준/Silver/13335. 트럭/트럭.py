from collections import deque

# n : 다리르 건너는 트럭의 수, w : 다리의 길이, l : 다리의 최대하중
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))     # 트럭의 무게

bridge = deque([0] * w)     # 다리

current_weight = 0      # 현재 다리 위의 무게
time = 0                # 경과 시간

waiting = deque(trucks)     # 대기 중인 트럭

# 모든 트럭이 다리를 건널 때까지 반복
while waiting or current_weight > 0:
    time += 1

    # 다리의 맨 앞 트럭(없으면 빈 공간) 제거
    out = bridge.popleft()
    current_weight -= out

    if waiting:
        # 무게 조건 확인
        if current_weight + waiting[0] <= L:
            # 트럭 진입
            truck = waiting.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            # 진입 불가 - 빈 공간 추가
            bridge.append(0)
    else:
        # 대기 트럭이 없으면 빈 공간 추가
        bridge.append(0)

print(time)