import sys

# 입출력 빠르게
input = sys.stdin.readline
print = sys.stdout.write

while True:
    # 문장 한 줄을 통째로 읽어옴
    line = input().rstrip()

    # 입력이 '.'이면 반복문 종료
    if line == '.':
        break

    # 스택 준비
    stack = []
    is_balanced = True # 균형이 맞는지 확인하는 플래그

    # 문장의 각 문자를 하나씩 확인
    for char in line:
        # 여는 괄호면 스택에 push
        if char == '(' or char == '[':
            stack.append(char)
        # 닫는 괄호일 때
        elif char == ')':
            # 스택이 비어있거나, 스택 맨 위가 짝이 안 맞으면 균형 안 맞음
            if not stack or stack[-1] != '(':
                is_balanced = False
                break # 더 이상 확인할 필요 없으니 반복 중단
            # 짝이 맞으면 스택에서 pop
            else:
                stack.pop()
        elif char == ']':
            # 스택이 비어있거나, 스택 맨 위가 짝이 안 맞으면 균형 안 맞음
            if not stack or stack[-1] != '[':
                is_balanced = False
                break # 반복 중단
            # 짝이 맞으면 스택에서 pop
            else:
                stack.pop()
        # 다른 문자들은 무시 (알파벳, 숫자, 공백 등)

    # 문자열 다 확인한 후에
    # 균형이 맞았고(is_balanced == True), 스택도 비어있으면 (모든 여는 괄호가 짝을 찾았으면)
    if is_balanced and not stack:
        print('yes\n')
    # 그 외의 모든 경우는 균형이 안 맞는 거임
    else:
        print('no\n')

