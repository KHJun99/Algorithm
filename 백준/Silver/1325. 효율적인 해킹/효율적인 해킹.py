from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def bfs(start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return len(visited)


N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

result = []
for idx in range(1, N + 1):
    result.append(bfs(idx))

max_val = max(result)
for i, val in enumerate(result):
    if val == max_val:
        print(i + 1, end = ' ')