# https://programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    rows = len(board)
    cols = len(board[0])

    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = board[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                max_side = max(max_side, dp[i][j])

    return max_side ** 2


print(solution([[i % 2 for i in range(1000)] for _ in range(1000)]))  # 4
print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 1
print(solution([[1], [1]]))  # 1
print(solution([[0], [0]]))  # 0
print(solution([[1, 1], [1, 1]]))  # 4
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4
