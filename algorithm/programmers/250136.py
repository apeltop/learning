from collections import deque, defaultdict


def solution(land):
    answer = 0

    oil_maps = []

    y, x = 0, 0
    while y < len(land):
        while x < len(land[0]):
            if land[y][x] == 0:
                x += 1
                continue

            q = deque([(y, x)])
            maps = []
            while q:
                target_y, target_x = q.popleft()
                if target_y >= len(land) or target_y < 0:
                    continue
                if target_x >= len(land[0]) or target_x < 0:
                    continue

                if land[target_y][target_x] == 0:
                    continue

                maps.append((target_y, target_x))
                land[target_y][target_x] = 0

                q.append((target_y, target_x + 1))
                q.append((target_y, target_x - 1))
                q.append((target_y + 1, target_x))
                q.append((target_y - 1, target_x))

            if maps:
                oil_maps.append(maps)
        x = 0
        y += 1

    oli_amount_by_col = defaultdict(int)
    for oil_map in oil_maps:
        amount = len(oil_map)
        for x in set(list(map(lambda yx : yx[1], oil_map))):
            oli_amount_by_col[x] += amount

    return max(oli_amount_by_col.values())


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]), 9)

print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
               ), 16)
