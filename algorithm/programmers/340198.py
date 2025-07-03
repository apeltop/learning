# https://school.programmers.co.kr/learn/courses/30/lessons/340198

def solution(mats, park):
    square_maps = [[0] * len(park[0]) for _ in range(len(park))]
    square_sizes = set()

    for y in range(len(park)):
        for x in range(len(park[y])):
            if park[y][x] == "-1":
                square_maps[y][x] = min(square_maps[y - 1][x - 1], square_maps[y - 1][x], square_maps[y][x - 1]) + 1
                square_sizes.add(square_maps[y][x])

    mats.sort(reverse=True)

    for mat in mats:
        if mat in square_sizes:
            return mat

    return -1


print(solution([5, 3, 2],
               [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]), 3)
