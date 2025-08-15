# 균형잡힌 세상
import sys
input = sys.stdin.readline
write = sys.stdout.write

parent = {
    ')' : '(',
    ']' : '['
}
while True:
    sen = input().rstrip()
    if sen == '.':
        break

    stack = []
    result = 'yes'

    for ch in sen:
        if ch in '([':
            stack.append(ch)
        elif ch in ')]':
            if not stack or stack.pop() != parent[ch]:
                result = 'no'
                break
    if stack:
        result = 'no'
    write(result + '\n')