from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    # 각 도시까지의 최단 거리를 저장할 배열
    # -1로 초기화하여 아직 방문하지 않은 상태를 구분
    dist = [-1] * (N + 1)
    dist[start] = 0         # 시작 도시는 거리 0으로 설정
    q = deque([start])

    # 결과로 반환할 도시 목록
    result = []

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if dist[nxt] == -1:                 # 아직 방문하지 않은 도시라면
                dist[nxt] = dist[cur] + 1       # 최단 거리 갱신
                q.append(nxt)                   # 큐에 추가하여 계속 탐색

    # 최단 거리가 정확히 K인 도시들을 결과에 저장
    for i in range(1, N + 1):
        if dist[i] == K:
            result.append(i)

    return result


N, M, K, X = map(int, input().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

citys = bfs(X)

if citys:
    citys.sort()
    print(*citys, sep='\n')
else:
    print(-1)