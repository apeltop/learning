import copy


def solution(rows, columns, queries):
    answer = []

    board = [[y * columns + x + 1 for x in range(columns)] for y in range(rows)]
    transBoard = [[y * columns + x + 1 for x in range(columns)] for y in range(rows)].copy()

    for query in queries:
        y1, x1, y2, x2 = query
        y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1

        mini = board[y1][x1]

        for x in range(x1, x2):
            transBoard[y1][x + 1] = board[y1][x]
            mini = min(mini, board[y1][x])

        for y in range(y1, y2):
            transBoard[y + 1][x2] = board[y][x2]
            mini = min(mini, board[y][x2])

        for x in range(x2, x1, -1):
            transBoard[y2][x - 1] = board[y2][x]
            mini = min(mini, board[y2][x])

        for y in range(y2, y1, -1):
            transBoard[y - 1][x1] = board[y][x1]
            mini = min(mini, board[y][x1])

        board = copy.deepcopy(transBoard)

        answer.append(mini)

    return answer


print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))  # [1, 1, 5, 3]
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))  # [8, 10, 25]
print(solution(100, 97, [[1, 1, 100, 97]]))  # [1]
