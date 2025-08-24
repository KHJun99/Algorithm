from collections import deque


def dfs(graph, start, visited, out):
    visited[start] = True
    out.append(start)
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(graph, nxt, visited, out)


def bfs(graph, start, n):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return order


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 방문 순서 규칙: 작은 번호부터
for i in range(1, N + 1):
    # 중복 간선 제거 + 정렬 (중복 없다고 확신하면 set() 없이 sorted만 해도 됨)
    graph[i] = sorted(set(graph[i]))

# DFS
visited = [False] * (N + 1)
dfs_order = []
dfs(graph, V, visited, dfs_order)

# BFS
bfs_order = bfs(graph, V, N)

print(*dfs_order)
print(*bfs_order)