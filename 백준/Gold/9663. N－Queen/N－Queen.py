import sys
input = sys.stdin.readline

def check(now_row):
    for i in range(now_row):
        # 같은 열에 있거나
        if chess[now_row] == chess[i]:
            return False
        
        # 대각선에 있으면
        # 열 차이 = 행 차이 => 대각선
        if abs(chess[now_row] - chess[i]) == abs(now_row - i):
            return False
    
    return True


def backtracking(queen_cnt):
    global result
    
    # 종료 조건 : N개 모두 배치 완료
    if queen_cnt == N:
        result += 1
        return
    
    # 현재 행의 모든 열을 시도
    for col in range(N):
        chess[queen_cnt] = col
        if check(queen_cnt):
            backtracking(queen_cnt + 1)


N = int(input())

chess = [-1] * N
result = 0

backtracking(0)

print(result)