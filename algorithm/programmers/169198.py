import math


def calc_min_distance(target, destination, axis):
    return math.ceil(
        (math.sqrt((axis[0] - target[0]) ** 2 + (axis[1] - target[1]) ** 2) +
         math.sqrt((axis[0] - destination[0]) ** 2 + (axis[1] - destination[1]) ** 2)) ** 2)


def solution(m, n, startX, startY, balls):
    answer = []

    candidate_xy = [
        (-startX, startY),
        (startX, n + (n - startY)),
        (m + (m - startX), startY),
        (startX, -startY),
    ]

    def calc_two_point_distance(target, destination):
        return (target[0] - destination[0]) ** 2 + (target[1] - destination[1]) ** 2

    for ball in balls:
        A, B = (startX, startY), ball
        min_distance = None

        for c_xy in candidate_xy:
            if (c_xy[1] - B[1]) == 0:
                if (c_xy[0] > B[0] > A[0]) or (c_xy[0] < B[0] < A[0]):
                    continue
            if (c_xy[0] - B[0]) == 0:
                if (c_xy[1] > B[1] > A[1]) or (c_xy[1] < B[1] < A[1]):
                    continue
            min_distance = min(min_distance, calc_two_point_distance(c_xy, B)) if min_distance else calc_two_point_distance(c_xy, B)
        answer.append(min_distance)
    return answer



print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))  # [52, 37, 116]
print(solution(10, 10, 7, 7, [[8, 7]]))  # [37]
