from collections import deque

# N: 동영상 개수, Q: 질문 개수
N, Q = map(int, input().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]

# N-1개의 간선 정보 입력
for _ in range(N-1):
    p, q, r = map(int, input().split())  # p-q 연결, 유사도 r
    graph[p].append((q, r))  # 양방향 그래프
    graph[q].append((p, r))


# Q개의 질문 처리
for _ in range(Q):
    k, v = map(int, input().split())  # k: 최소 유사도 기준, v: 시작 동영상

    # 방문 체크 배열
    visited = [False] * (N + 1)
    # BFS를 위한 큐
    queue = deque()
    # 추천 가능한 동영상 개수
    cnt = 0

    # 시작 노드 설정
    visited[v] = True
    # (현재 노드, 여기까지 오는 경로의 최솟값) - 시작은 무한대
    queue.append((v, float('inf')))

    # BFS 탐색 시작
    while queue:
        # 현재 노드와 여기까지의 USADO 값 꺼내기
        cur_node, min_usado = queue.popleft()

        # 현재 노드와 연결된 모든 노드 확인
        for next_node, edge_usado in graph[cur_node]:
            
            # 이미 방문한 노드는 건너뛰기
            if visited[next_node]:
                continue
            
            visited[next_node] = True  # 방문 처리

            # 다음 노드까지의 USADO 계산
            # = 지금까지의 최솟값과 현재 간선 유사도 중 최솟값
            new_usado = min(min_usado, edge_usado)

            # USADO가 k 이상이면 추천 가능
            if new_usado >= k:
                cnt += 1  # 추천 가능한 동영상 개수 증가
                queue.append((next_node, new_usado))  # 큐에 추가하여 계속 탐색
            # k 미만이면 더 이상 그 방향으로 탐색하지 않음

    print(cnt) 