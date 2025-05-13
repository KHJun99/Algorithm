import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

stack = []

for _ in range(n):
    command = list(map(int, input().split()))   # 명령을 읽어서 리스트로 만듦

    if command[0] == 1:
        # command[0]이 1이면 뒤에 숫자 X가 따라옴
        stack.append(command[1])
    elif command[0] == 2:
        # command[0]이 2이면 스택에서 뺌
        if stack:   # 스택이 비어있지 않으면
            print(str(stack.pop()) + '\n')
        else:       # 스택이 비어있으면
            print('-1\n')
    elif command[0] == 3:
        # command[0]이 3이면 스택 사이즈 출력
        print(str(len(stack)) + '\n')
    elif command[0] == 4:
        # command[0]이 4이면 스택 비었는지 확인
        if not stack:   # 스택이 비어있으면
            print('1\n')
        else:           # 스택이 비어있지 않으면
            print('0\n')
    elif command[0] == 5:
        # command[0]이 5이면 스택 맨 위 값 추력
        if stack:   # 스택이 비어있지 않으면
            print(str(stack[-1]) + '\n')
        else:       # 스택이 비어있으면
            print('-1\n')