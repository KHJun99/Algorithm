# [파이썬 S/W 문제해결 기본] 3일차 - 회문

# 회문 판별 함수
def is_palindrome(matrix, n, m):
    # 행 순환   
    for r in range(n):
        # (n - m + 1)인 이유 : 인덱스를 벗어나지 않게 하기 위해
        for idx in range(n - m + 1):  
            word = matrix[r][idx: idx + m]
            if word == word[::-1]:
                return word
                            
    # 열 순환
    for idx in range(n):
        for r in range(n - m + 1):
            word = ''.join(matrix[x][idx] for x in range(r, r + m))
            if word == word[::-1]:
                return word
    
    return None        

t = int(input())

for i in range(1, t + 1):
    n, m = map(int,input().split())
    matrix = []
    
    for _ in range(n):
        matrix.append(input())
        
    result = is_palindrome(matrix, n, m)

    if result:
        print(f'#{i} {result}')

