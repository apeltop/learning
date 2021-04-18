import math


def solution(arr):
    def compress(x1, y1, x2, y2):
        side_length = x2 - x1

        compress(x1, y1, math.floor(x2 / 2), math.floor(y2 / 2))
        compress(x1, math.ceil(y1 / 2), math.floor(x1 / 2), x2)

        return

    arr_len = len(arr)
    answer = compress(0, arr_len - 1, 0, arr_len - 1)
    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))  # [4,9]
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))  # [10,15]
