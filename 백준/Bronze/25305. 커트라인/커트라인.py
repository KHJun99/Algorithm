n, k = map(int, input().split())

score = list(map(int, input().split()))

score.sort(reverse=True)        # 오름차순 정렬 (reverse = False, 내림차순)

print(score[k-1])