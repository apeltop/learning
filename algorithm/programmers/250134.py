# https://school.programmers.co.kr/learn/courses/30/lessons/250134
from collections import deque
from itertools import product


def solution(maze):
    def bfs():
        min_dist = float('inf')
        red_yx, blue_yx, target_red_yx, target_blue_yx = (0, 0), (0, 0), (0, 0), (0, 0)

        move_pos = list(product([(-1, 0), (1, 0), (0, 1), (0, -1)], repeat=2))

        for y, row in enumerate(maze):
            for x, col in enumerate(row):
                if col == 1:
                    red_yx = (y, x)
                if col == 2:
                    blue_yx = (y, x)
                if col == 3:
                    target_red_yx = (y, x)
                if col == 4:
                    target_blue_yx = (y, x)

        q = deque([((red_yx[0], red_yx[1]), (blue_yx[0], blue_yx[1]), {}, {})])

        while q:
            red_yx, blue_yx, red_history, blue_history = q.popleft()

            if min_dist <= len(red_history):
                continue

            if red_yx == target_red_yx and blue_yx == target_blue_yx:
                if max(len(red_history), len(blue_history)) < min_dist:
                    min_dist = max(len(red_history), len(blue_history))
                continue

            if (red_yx[0] < 0 or red_yx[0] >= len(maze)) or (red_yx[1] < 0 or red_yx[1] >= len(maze[0])):
                continue
            if (blue_yx[0] < 0 or blue_yx[0] >= len(maze)) or (blue_yx[1] < 0 or blue_yx[1] >= len(maze[0])):
                continue
            if maze[red_yx[0]][red_yx[1]] == 5 or maze[blue_yx[0]][blue_yx[1]] == 5:
                continue
            if (red_yx != target_red_yx and ''.join(map(str, list(red_yx))) in red_history) or (
                    blue_yx != target_blue_yx and ''.join(map(str, list(blue_yx))) in blue_history):
                continue
            if red_yx == blue_yx:
                continue

            red_history[''.join(map(str, list(red_yx)))] = True
            blue_history[''.join(map(str, list(blue_yx)))] = True

            for v in move_pos:
                next_red_yx = red_yx if red_yx == target_red_yx else (red_yx[0] + v[0][0], red_yx[1] + v[0][1])
                next_blue_yx = blue_yx if blue_yx == target_blue_yx else (blue_yx[0] + v[1][0], blue_yx[1] + v[1][1])

                if next_red_yx == blue_yx and next_blue_yx == red_yx:
                    continue

                q.append((next_red_yx, next_blue_yx, dict(red_history), dict(blue_history)))
        return min_dist

    answer = bfs()
    return 0 if answer == float('inf') else answer


print(solution([[1, 4], [0, 0], [2, 3]]), 3)
print(solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]), 7)
print(solution([[1, 5], [2, 5], [4, 5], [3, 5]]), 0)
print(solution([[4, 1, 2, 3]]), 0)
