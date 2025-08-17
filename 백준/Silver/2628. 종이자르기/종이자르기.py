# 종이 자르기
width, length = map(int, input().split())
T = int(input())


# 가로(수평) 절단선: 세로 길이 방향 좌표(0과 length 포함)
h = [0, length]
# 세로(수직) 절단선: 가로 길이 방향 좌표(0과 width 포함)
v = [0, width]

for _ in range(T):
    a, b = map(int, input().split())
    if a == 0:      # 가로(수평)로 자르기 → 세로 방향 좌표 리스트(h)에 추가
        h.append(b)
    else:           # 세로(수직)로 자르기 → 가로 방향 좌표 리스트(v)에 추가
        v.append(b)

h.sort()
v.sort()


# 인접 절단선 사이의 최대 간격(=조각의 최대 높이/너비)
max_h = max(h[i + 1] - h[i] for i in range(len(h) - 1))
max_w = max(v[i + 1] - v[i] for i in range(len(v) - 1))

print(max_h * max_w)