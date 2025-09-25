import heapq
import sys

input = sys.stdin.readline

# V : 정점의 개수, E : 간선의 개수
V, E = map(int, input().split())
# K : 시작 정점의 번호
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    # u : 시작 , v : 도착, w : 가중치
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

LIMIT = 20001
INF = 10 ** 15
dist = [INF] * (LIMIT + 1)
dist[K] = 0

pq = [(0, K)]
while pq:
    cur_dist, u = heapq.heappop(pq)
    if cur_dist > dist[u]:
        continue

    for v, w in graph[u]:
        if dist[v] > cur_dist + w:
            dist[v] = cur_dist + w
            heapq.heappush(pq, (dist[v], v))

for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
