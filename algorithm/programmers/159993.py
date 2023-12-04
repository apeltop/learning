# https://school.programmers.co.kr/learn/courses/30/lessons/159993
import copy
from collections import deque


def solution(maps):
    answer = 0

    def find_by_bfs(start_xy, destination_xy):
        q = deque([])
        q.append((start_xy, -1))

        visited_xy = set()

        while q:
            xy, history_count = q.popleft()
            x, y = xy

            if xy in visited_xy:
                continue

            if x < 0 or x >= len(maps[0]):
                continue
            if y < 0 or y >= len(maps):
                continue

            if maps[y][x] == 'X':
                continue

            visited_xy.add(xy)
            history_count += 1

            if (x, y) == destination_xy:
                return history_count

            q.append(((x + 1, y), history_count))
            q.append(((x, y + 1), history_count))
            q.append(((x - 1, y), history_count))
            q.append(((x, y - 1), history_count))

        return -1

    s_xy = l_xy = e_xy = (0, 0)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s_xy = (j, i)
            if maps[i][j] == 'L':
                l_xy = (j, i)
            if maps[i][j] == 'E':
                e_xy = (j, i)

    s_to_l = find_by_bfs(s_xy, l_xy)
    l_to_e = find_by_bfs(l_xy, e_xy)

    if s_to_l == -1 or l_to_e == -1:
        return -1

    return s_to_l + l_to_e


print(solution(["SOOOOOOOOL", "XXXXOOOOOO", "OOOOOOOOOO", "OXXXXOOOOO", "OOOOOOOOOE"]))  # 13
print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))  # 16
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))  # -1
