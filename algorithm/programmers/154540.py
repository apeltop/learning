# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque


def solution(maps):
    answer = []

    maps_2d = [[maps[i][j] for j in range(len(maps[0]))] for i in range(len(maps))]

    def calc_food(yx):
        q = deque([])
        q.append((yx))
        total = 0

        while q:
            yx = q.popleft()
            y, x = yx

            if y >= len(maps_2d) or y < 0:
                continue

            if x >= len(maps_2d[0]) or x < 0:
                continue

            if maps_2d[y][x] == 'X' or maps_2d[y][x] == 0:
                continue

            total += int(maps_2d[y][x])
            maps_2d[y][x] = 0

            q.append((y + 1, x))
            q.append((y - 1, x))
            q.append((y, x + 1))
            q.append((y, x - 1))
        return total

    for i in range(len(maps_2d)):
        for j in range(len(maps_2d[0])):
            if maps_2d[i][j] != 'X' and maps_2d[i][j] != 0:
                answer.append(calc_food((i, j)))

    return sorted(answer) if answer else [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]), [1, 1, 27])
print(solution(["11111", "11111", "11111", "11111"]), [20])
print(solution(["11111", "11X11", "11111", "1111X"]), [18])
print(solution(["11111", "11X11", "1111X", "1111X"]), [17])
print(solution(["XXX", "XXX", "XXX"]), [-1])

print(solution(
    ["X591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591XX591X" for _ in
     range(100)]), [1, 1, 27])

print(solution(
    ["1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890" for _ in
     range(100)]), [1, 1, 27])
