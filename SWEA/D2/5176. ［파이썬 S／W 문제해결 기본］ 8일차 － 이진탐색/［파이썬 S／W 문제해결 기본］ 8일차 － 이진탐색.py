# 중위 순회 함수
def inorder_arr(tree, i, out):
    # 범위 밖이거나 비어있으면 종료
    if i >= len(tree) or tree[i] is None:
        return
    inorder_arr(tree, 2*i, out)       # 왼쪽
    out.append(tree[i])               # 현재
    inorder_arr(tree, 2*i+1, out)     # 오른쪽


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bt = []
    for i in range(N + 1):
        bt.append(i)
    res = []
    inorder_arr(bt, 1, res)
    inorder_lst = [0] * (N + 1)
    for k, idx in enumerate(res, start=1):
        inorder_lst[idx] = k

    print(f'#{tc} {inorder_lst[1]} {inorder_lst[N // 2]}')