from itertools import combinations


def solution(n, q, ans):

    return sum(
        all(len([v for v in q[i] if v in comb]) == ans[i] for i in range(len(q)))
        for comb in combinations([i + 1 for i in range(n)], 5)
    )


print(
    solution(
        10,
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [3, 7, 8, 9, 10],
            [2, 5, 7, 9, 10],
            [3, 4, 5, 6, 7],
        ],
        [2, 3, 4, 3, 3],
    ),
    3,
)

print(
    solution(
        15,
        [
            [2, 3, 9, 12, 13],
            [1, 4, 6, 7, 9],
            [1, 2, 8, 10, 12],
            [6, 7, 11, 13, 15],
            [1, 4, 10, 11, 14],
        ],
        [2, 1, 3, 0, 1],
    ),
    5,
)

print(
    solution(
        30,
        [
            [2, 3, 9, 12, 13],
            [1, 4, 6, 7, 9],
            [1, 2, 8, 10, 12],
            [6, 7, 11, 13, 15],
            [1, 4, 10, 11, 14],
            [1, 4, 10, 11, 14],
            [1, 4, 10, 11, 14],
            [1, 4, 10, 11, 14],
            [1, 4, 10, 11, 14],
            [1, 4, 10, 11, 14],
        ],
        [2, 1, 3, 0, 1, 1, 1, 1, 1, 1],
    ),
    200,
)
