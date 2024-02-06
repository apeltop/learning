def solution(rows, columns, queries):
    answer = []

    maps = [((row * columns + col) + 1) for row in range(rows) for col in range(columns)]

    for query in queries:
        y1, x1, y2, x2 = map(lambda x: x - 1, query)

        border1 = [(y1, x) for x in range(x1, x2 + 1)]
        border2 = [(y, x2) for y in range(y1, y2 + 1)][1:-1]
        border3 = list(map(lambda yx: (y2, yx[1]), border1))
        border4 = list(map(lambda yx: (yx[0], x1), border2))

        border3.reverse()
        border4.reverse()

        borders = border1 + border2 + border3 + border4 + [border1[0]]
        values = list(map(lambda yx: maps[yx[0] * columns + yx[1]], borders))

        for i in range(1, len(borders)):
            y, x = borders[i]
            maps[y * columns + x] = values[i - 1]

        answer.append(sorted(values)[0])

    return answer


print(solution(6, 5, [[1, 1, 6, 5]]))
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]), [8, 10, 25])
print(solution(100, 97, [[1, 1, 100, 97]]), [1])
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]), [1, 1, 5, 3])
