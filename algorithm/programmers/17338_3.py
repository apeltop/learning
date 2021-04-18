import collections


def solution(v):
    def checkFarm(y, x, crop):
        if crop == v[y][x]:
            v[y][x] = -1
        else:
            return

        if not y == 0:
            checkFarm(y - 1, x, crop)
        if not y == len(v) - 1:
            checkFarm(y + 1, x, crop)
        if not x == 0:
            checkFarm(y, x - 1, crop)
        if not x == len(v[y]) - 1:
            checkFarm(y, x + 1, crop)

        return crop

    answer = []
    count = collections.defaultdict(int)

    for i in range(len(v)):
        for j in range(len(v[i])):
            if v[i][j] == -1:
                continue

            count[checkFarm(i, j, v[i][j])] += 1

    answer.append(count[0])
    answer.append(count[1])
    answer.append(count[2])

    return answer


print(solution([[0, 0, 1, 1], [1, 1, 1, 1], [2, 2, 2, 1], [0, 0, 0, 2]]))  # [2,1,2]
print(solution([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))  # [3, 2]
print(solution([[0, 0, 1], [2, 2, 1], [0, 0, 0]]))  # [2,1,1]
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # [2,1,1]
print(solution([[1], [1]]))  # [1]
