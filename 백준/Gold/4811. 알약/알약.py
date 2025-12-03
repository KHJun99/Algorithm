memo = {}
def solve(w, h):
    """
    :param w: 병에 남은 온전한 알약 개수 
    :param h: 병에 남은 반 조각 개수
    :return: 이 상태에서 끝까지 가는 경우의 수
    """
    # 병이 비었으면 1가지 방법
    if w == 0 and h == 0:
        return 1
    
    # 이미 계산한 적 있으면 저장된 값 반환
    if (w, h) in memo:
        return memo[(w, h)]

    result = 0
    
    # 온전한 알약을 꺼낼 수 있으면
    if w > 0:
        result += solve(w - 1, h + 1)   # W 기록
    
    # 반조각을 꺼낼 수 있으면 
    if h > 0:
        result += solve(w, h - 1)   # H 기록
    
    # 결과 메모이제이션
    memo[(w, h)] = result
    return result


while True:
    N = int(input())

    if N == 0:
        break
    
    # 메모 초기화 (각 테스트마다)
    memo = {}
    
    # 초기값 : 온전한 알약 N개, 반 조각 0개
    answer = solve(N, 0)
    print(answer)