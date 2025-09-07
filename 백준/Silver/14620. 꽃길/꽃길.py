def flower_sum_with_cells(lst):
    """각 후보의 (순서, 비용, 점유좌표집합)을 반환"""
    N = len(lst)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    items = []
    i = 1
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            cells = {(r, c)}
            cost = lst[r][c]
            ok = True
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    cells.add((nr, nc))
                    cost += lst[nr][nc]
                else:
                    ok = False
                    break
            if ok:
                items.append((i, cost, cells))
            i += 1
    return items  # [(idx, cost, cells), ...]


def no_overlap(idx_a, idx_b, idx_to_cells):
    """두 후보가 겹치지 않으면 True"""
    return idx_to_cells[idx_a].isdisjoint(idx_to_cells[idx_b])


def comb_no_overlap(m, idx_to_cells):
    """1..m에서 3개 고르되, 셋 모두 서로 겹치지 않는 조합만"""
    res = []
    for a in range(1, m + 1):
        for b in range(a + 1, m + 1):
            if not no_overlap(a, b, idx_to_cells):
                continue
            for c in range(b + 1, m + 1):
                if no_overlap(a, c, idx_to_cells) and no_overlap(b, c, idx_to_cells):
                    res.append((a, b, c))
    return res


# ---------- 실행부 ----------
N = int(input().strip())
flower = [list(map(int, input().split())) for _ in range(N)]

# (순서, 합, 좌표집합)
items = flower_sum_with_cells(flower)

# 매핑 준비
idx_to_cost = {}
idx_to_cells = {}
for idx, cost, cells in items:
    idx_to_cost[idx] = cost
    idx_to_cells[idx] = cells

m = len(items)

# '겹침 없음' 조건의 유효 조합
valid_triples = comb_no_overlap(m, idx_to_cells)

# 각 조합의 총 비용 계산 후 최소 출력
ans = None
for a, b, c in valid_triples:
    s = idx_to_cost[a] + idx_to_cost[b] + idx_to_cost[c]
    if ans is None or s < ans:
        ans = s

print(ans if ans is not None else "불가능")