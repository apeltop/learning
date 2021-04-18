# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0

    def findRectangle(y, x, k):
        maxK = 0

        if k == 1:
            return board[y][x]

        isRect = True
        for i in range(y, k):
            if not isRect:
                break
            for j in range(x, k):
                if not isRect:
                    break
                if board[i][j] == 0:
                    isRect = False

        if isRect:
            maxK = k * k
        else:
            for i in range(y, k - 1):
                for j in range(x, k - 1):
                    maxK = max(maxK, findRectangle(i, j, k - 1))
        return maxK

    for a in range(len(board)):
        for b in range(len(board[0])):
            if board[a][b] == 0:
                break
            answer = max(answer, findRectangle(a, b, min(len(board), len(board[0]))))

    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 1
print(solution([[1], [1]]))  # 1
print(solution([[0], [0]]))  # 0
print(solution([[1, 1], [1, 1]]))  # 0
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4
