from collections import deque    

def solution(maps):
    answer = []
    
    queue = deque()
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for r in range(n):
        for c in range(m):
            tmp = 0
            if maps[r][c] != 'X' and not visited[r][c]:
                queue.append((r, c))
                visited[r][c] = True
                tmp += int(maps[r][c])
                
                while queue:
                    cx, cy = queue.popleft()
                    
                    for dx, dy in delta:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and maps[nx][ny] != 'X':
                                tmp += int(maps[nx][ny])
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                answer.append(tmp)
    if len(answer) == 0:
        answer.append(-1)
    
    return sorted(answer)