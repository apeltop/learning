def solution(board):
    answer = 0

    for length in range(min(len(board), len(board[0])), 0, -1):
        for i in range(0, len(board) - length + 1):
            for j in range(0, len(board[0]) - length + 1):

                isSquare = True
                for y in range(i, i+length):
                    if not isSquare:
                        break

                    for x in range(j, j+length):
                        if board[y][x] == 0:
                            isSquare = False
                if isSquare:
                    return length * length

    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4
print(solution([[1], [1]]))  # 1
print(solution([[1, 1, 0], [1, 1, 0]]))  # 4
