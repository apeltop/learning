# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for y in range(0, len(land) - 1):
        row = land[y]

        order_row = sorted(row)[::]
        max_1, max_2 = order_row[-1], order_row[-2]
        max_1_i, max_2_i = row.index(max_1), row.index(max_2)
        indexes = [0, 1, 2, 3]
        indexes.remove(max_1_i)

        for index in indexes:
            land[y + 1][index] += max_1
        land[y + 1][max_1_i] += max_2

    return max(land[-1])


print(solution([
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [4, 3, 2, 1]]),
    16)

print(solution([
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [4, 3, 2, 100]]),
    112)