from collections import deque


def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])
    result = []

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    for i in range(1, N + 1):
        if dist[i] == K:
            result.append(i)

    return result


# T = int(input())
# for tc in range(T):
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

citys = bfs(X)
citys.sort()
if citys:
    for i in citys:
        print(i)
else:
    print(-1)