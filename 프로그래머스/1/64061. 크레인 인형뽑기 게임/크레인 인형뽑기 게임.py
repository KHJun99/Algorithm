def solution(board, moves):
    answer = 0
    n = len(board)
    
    stack = []

    for idx in moves:
        for r in range(n):
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
                
            if board[r][idx - 1] != 0:
                stack.append(board[r][idx - 1])
                board[r][idx - 1] = 0
                break
            
    return answer