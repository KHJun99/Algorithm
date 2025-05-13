import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

for _ in range(n):  # N번 반복하면서 각 문자열을 독립적으로 처리
    vp = str(input()).strip()  # 문자열 하나 입력받고 공백 제거

    count = 0  # <<< ★★★ 각 문자열 처리 시작할 때마다 count를 0으로 초기화! ★★★
    is_vps = True  # <<< 이 문자열이 올바른지 체크할 플래그

    for char in vp:  # 문자열의 각 글자를 스캔
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        # ★★★ 괄호 밸런스가 깨졌는지 중간중간 체크! ★★★
        if count < 0:  # 닫는 괄호가 먼저 나온 경우
            is_vps = False  # 올바른 괄호 문자열 아님!
            break  # 이 문자열은 더 볼 필요 없음. 다음 문자열로 넘어가자!

    # ★★★ 문자열 스캔이 끝난 후 최종 판단 ★★★
    if is_vps and count == 0:  # 중간에 밸런스 안 깨졌고, 최종 괄호 개수도 맞으면 (count가 0)
        print('YES\n')
    else:  # 중간에 밸런스 깨졌거나 (is_vps가 False), 최종 count가 0이 아니면
        print('NO\n')