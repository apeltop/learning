def solution(board):
    answer = 0
    max_side = min(len(board), len(board[0]))

    for side_length in range(max_side, 0, -1):
        for i in range(len(board)):
            if len(board) < i + side_length:
                continue
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    continue
                if len(board[0]) < j + side_length:
                    break

                isSquare = True
                for slice_i in range(i, side_length+i):
                    if not isSquare:
                        break
                    for slice_j in range(j, side_length+j):
                        if not isSquare:
                            break
                        if board[slice_i][slice_j] == 0:
                            isSquare = False

                if isSquare:
                    return side_length * side_length

    return answer


print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))  # 16
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 1
print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4
print(solution([[0], [1]]))  # 1
print(solution([[0], [0]]))  # 0
