# 재귀의 동작을 파악하는 문제
import sys

input = sys.stdin.readline

def recursion(s, l, r, count):
    count[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1, count)

def isPalindrome(s):
    count = [0]
    result = recursion(s, 0, len(s) - 1, count)
    return result, count[0]


t = int(input())

for i in range(t):
    Str = input().strip()
    result, count = isPalindrome(Str)
    print(result, count)
    