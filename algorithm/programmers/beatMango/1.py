# https://programmers.co.kr/tryouts/21474/challenges
import collections
from functools import reduce


def solution(board):
    def dfs(rowIndex, colIndex, uId):
        if board[rowIndex][colIndex] != uId[0]:
            return 0
        board[rowIndex][colIndex] = uId

        count = 1

        if colIndex != 0:
            count += dfs(rowIndex, colIndex - 1, uId)
        if colIndex != len(board[0]) - 1:
            count += dfs(rowIndex, colIndex + 1, uId)
        if rowIndex != 0:
            count += dfs(rowIndex - 1, colIndex, uId)
        if rowIndex != len(board) - 1:
            count += dfs(rowIndex + 1, colIndex, uId)

        return count

    board = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]
    blockDict = collections.defaultdict(int)

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if '_' not in board[i][j]:
                blockDict[f'{col}_{i}_{j}'] = dfs(i, j, f'{col}_{i}_{j}')

    maxCount = 0
    for row in board:
        count = reduce(lambda x, y: x + y, list(map(lambda x: blockDict[x], list(set(row)))))
        if count == len(board) * len(board[0]):
            return count
        maxCount = max(maxCount, count)

    return maxCount


print(solution(["ABBBBC", "AABAAC", "BCDDAC", "DCCDDE", "DCCEDE", "DDEEEB"]))  # 20
print(solution(["DDCCC", "DBBBC", "DBABC", "DBBBC", "DDCCC"]))  # 25
print(solution(["AAA", "AAA", "AAA"]))  # 25
