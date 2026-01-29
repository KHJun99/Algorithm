from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([i, p] for i, p in enumerate(priorities))
    
    cnt = 0
    while queue:
        current_i, current_p = queue.popleft()
        
        if any(current_p < q[1] for q in queue):
            queue.append((current_i, current_p))
        else:
            cnt += 1
            if current_i == location:
                return cnt
    
    return answer