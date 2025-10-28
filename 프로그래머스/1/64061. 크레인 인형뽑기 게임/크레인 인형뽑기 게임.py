def solution(board, moves):
    answer = 0
    n = len(board)
    
    stack = []
    
    # moves 순서대로 진행
    for idx in moves:
        # 행을 순환하면서 인형이 있으면 stack에 넣는 과정
        for r in range(n):
            # stack의 -1번 인덱스와 -2번 인덱스가 같으면 둘다 pop() 후
            # answer += 2
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
            
            # 인형이 있으면 스택에 인형을 삽입
            if board[r][idx - 1] != 0:
                stack.append(board[r][idx - 1])
                # 인형을 기존 위치에서 뽑았기 때문에 0으로 초기화
                board[r][idx - 1] = 0
                # break를 하지 않으면 모든 열의 인형을 다 뽑기 때문에 필수
                break
            
    return answer