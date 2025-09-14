dwarf = [int(input().strip()) for _ in range(9)]
dwarf.sort()  # 정답은 오름차순 출력 요구

selected = []


def dfs(i, cnt, total):
    # 7명 선택 완료
    if cnt == 7:
        if total == 100:
            print("\n".join(map(str, selected)))  # 한 줄에 하나씩 출력(BOJ 형식)
            return True  # 찾았으니 즉시 종료 신호
        return False

    # 인덱스 초과 또는 합 초과 시 가지치기
    if i == 9 or total > 100:
        return False

    # 1) i번째 난쟁이 선택
    selected.append(dwarf[i])
    if dfs(i + 1, cnt + 1, total + dwarf[i]):
        return True
    selected.pop()

    # 2) i번째 난쟁이 선택 안 함
    if dfs(i + 1, cnt, total):
        return True

    return False


dfs(0, 0, 0)