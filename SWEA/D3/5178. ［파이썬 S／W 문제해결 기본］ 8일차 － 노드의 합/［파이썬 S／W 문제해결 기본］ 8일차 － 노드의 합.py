def find_node_val(tree, L, N):
    # 범위 밖이면 0
    if L > N:
        return 0
    # 리프(자식 없음)이면 현재 값 반환
    if L * 2 > N:
        return tree[L]
    # 내부 노드: 자식 합으로 채움
    left = find_node_val(tree, L * 2, N)
    right = find_node_val(tree, L * 2 + 1, N)
    tree[L] = left + right
    return tree[L]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    bt = [0] * (N + 1)  # 0으로 초기화
    for _ in range(M):
        idx, val = map(int, input().split())
        bt[idx] = val

    result = find_node_val(bt, L, N)
    print(f'#{tc} {result}')