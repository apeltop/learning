from collections import defaultdict


def solution(points, routes):
    answer = 0

    def calc_path(yx1, yx2):
        yx1 = yx1[::]
        paths = []

        while not (yx1[0] == yx2[0] and yx1[1] == yx2[1]):
            if yx1[0] != yx2[0]:
                yx1[0] += 1 if yx1[0] < yx2[0] else -1
            elif yx1[1] != yx2[1]:
                yx1[1] += 1 if yx1[1] < yx2[1] else -1

            paths.append(yx1[::])
        return paths

    map_dict = defaultdict(int)
    paths = []
    max_path_length = 0
    for route in routes:
        path = [points[route[0] - 1]][::]
        for i in range(0, len(route) -1):
            path.extend(calc_path(points[route[i] - 1], points[route[i + 1] - 1]))

        max_path_length = max(max_path_length, len(path))
        paths.append(path)

    for i in range(max_path_length):
        for path in paths:
            if i == len(path):
                map_dict[f'{path[-1][0]}_{path[-1][1]}'] -= 1
                continue

            if i > len(path):
                continue

            map_dict[f'{path[i][0]}_{path[i][1]}'] += 1

            if i == 0:
                continue

            map_dict[f'{path[i - 1][0]}_{path[i - 1][1]}'] -= 1
            if map_dict[f'{path[i - 1][0]}_{path[i - 1][1]}'] == 0:
                del map_dict[f'{path[i - 1][0]}_{path[i - 1][1]}']

        for k, v in map_dict.items():
            if 1 < v:
                answer += 1

    return answer



print(solution([[1, 1], [1, 4]], [[1, 2, 1, 2], [1, 2, 1, 2], [1, 2]]), 10)
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]), 0)
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]), 9)
print(solution([[1, 1], [1, 4]], [[1, 2], [2, 1]]), 0)
print(solution([[1, 1], [1, 5]], [[1, 2], [2, 1]]), 1)
print(solution([[1, 1], [1, 4]], [[1, 2], [1, 2]]), 4)
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]), 1)
