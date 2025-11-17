from collections import deque


def rock_game(a, b, c):
    queue = deque([(a, b, c, 0)])
    visited = set()
    visited.add((a, b, c))

    while queue:
        n1, n2, n3, turn = queue.popleft()

        if n1 == n2 == n3:
            return 1

        if turn % 2 == 0:
            if n1 != n2:
                if n1 > n2:
                    new_state = (n1 - n2, n2 * 2, n3)
                else:
                    new_state = (n1 * 2, n2 - n1, n3)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((*new_state, turn + 1))
            else:
                queue.append((n1, n2, n3, turn + 1))
        else:
            if n2 != n3:
                if n2 > n3:
                    new_state = (n1, n2 - n3, n3 * 2)
                else:
                    new_state = (n1, n2 * 2, n3 - n2)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((*new_state, turn + 1))
            else:
                queue.append((n1, n2, n3, turn + 1))
    return 0


A, B, C = map(int, input().split())

print(rock_game(A, B, C))