from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    delta = [(0, 1), (1, 0), (-1, 0), (-1, 0)]
    
    graph = [[] for _ in range(n + 1)]
    # 양방향
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n + 1)
    # 부대위치 = 0
    distance[destination] = 0
    
    # bfs
    queue = deque([destination])
    while queue:
        current = queue.popleft()
        
        for next_node in graph[current]:
            if distance[next_node] == -1:
                distance[next_node] = distance[current] + 1
                queue.append(next_node)
    
    for source in sources:
        answer.append(distance[source])

    return answer