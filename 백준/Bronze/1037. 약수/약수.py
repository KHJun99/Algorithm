# 1과 N 빼고 다 주어졌을 때 N을 찾는 문제
import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

print(max(num) * min(num))