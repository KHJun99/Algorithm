# 인사성 밝은 곰곰이
import sys

input = sys.stdin.readline

n = int(input())

total_greetings = 0 # 전체 인사 횟수
current_session_users = set() # 현재 ENTER 이후 메시지를 보낸 유저들을 저장할 집합

for _ in range(n):
    user_input = input().strip() # 입력 읽고 앞뒤 공백/개행문자 제거!

    if user_input == 'ENTER':
        # ENTER를 만나면 현재까지 쌓인 유저 수를 총 인사 횟수에 더하고
        total_greetings += len(current_session_users)
        # 현재 세션 유저 목록을 초기화!
        current_session_users = set()
    else:
        # 유저 ID면 현재 세션 유저 집합에 추가 (중복 자동 처리)
        current_session_users.add(user_input)

# 모든 입력을 다 읽고 나서, 마지막 ENTER 이후에 쌓인 유저들이 있다면
# 그 유저들도 인사를 한 것이므로 총 인사 횟수에 마지막으로 더해준다.
total_greetings += len(current_session_users)

print(total_greetings) # 최종 인사 횟수 출력!
