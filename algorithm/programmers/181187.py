import math


def points_in_circle(radius):
    r = radius
    res = 0
    outlines = 0
    r2 = r * r

    for y in range(r + 1):
        v = int(math.sqrt(r2 - y * y))
        res += v

        if v > 0 and v == math.sqrt(r2 - y * y):
            outlines += 1

    return res * 4 + 1, outlines * 4


def solution(r1, r2):
    p1, o1 = points_in_circle(r1)
    p2, o2 = points_in_circle(r2)
    return p2 - p1 + o1


print(points_in_circle(1))
print(points_in_circle(2))
print(points_in_circle(3))
print(points_in_circle(4))
print(points_in_circle(5))
print(points_in_circle(6))
print()


def points_in_circle2(radius):
    r = radius
    res = 0
    for i in range(r + 1):
        for j in range(1, r + 1):
            if i * i + j * j == r * r:
                res += 1

    res = res * 4

    return res


print(points_in_circle2(1))
print(points_in_circle2(2))
print(points_in_circle2(3))
print(points_in_circle2(4))
print(points_in_circle2(5))
print(points_in_circle2(6))
print()
print(solution(1, 2))  # 12
print(solution(1, 3))  # 28
print(solution(1, 4))  # 48
print(solution(2, 3))  # 20
print(solution(2, 6))  # 104

# v1
# def solution(r1, r2):
#     answer = 0
#     DEFAULT_DOT = 4
#
#     for i in range(r2, 0, -1):
#         if i == r1:
#             break
#         number_of_points_on_a_side = (i * 2) - 1
#         answer += (number_of_points_on_a_side * 4) - 4
#         # print(i, (number_of_points_on_a_side * 4) - 4)
#
#     return answer + (DEFAULT_DOT)


# v2
# def points_in_circle(radius):
#     result = set()
#     for x, y in product(range(int(radius) + 1), repeat=2):
#         if x ** 2 + y ** 2 <= radius ** 2:
#             result.add((x, y))
#             result.add((x, -y))
#             result.add((-x, y))
#             result.add((-x, -y))
#     return len(result)
#
#
# def solution(r1, r2):
#     # print(r2, points_in_circle(r2))
#     # print(r1, points_in_circle(r1))
#     return points_in_circle(r2) - points_in_circle(r1) + 4

# v3
# point_dict = collections.defaultdict(int)
# point_outline_dict = collections.defaultdict(int)
#
#
# def points_in_circle(radius):
#     result = set()
#     result_outline = set()
#
#     if radius in point_dict:
#         return
#
#     for x, y in product(range(int(radius) + 1), repeat=2):
#         if x ** 2 + y ** 2 == radius ** 2:
#             result_outline.add((x, y))
#             result_outline.add((x, -y))
#             result_outline.add((-x, y))
#             result_outline.add((-x, -y))
#
#         if x ** 2 + y ** 2 <= radius ** 2:
#             result.add((x, y))
#             result.add((x, -y))
#             result.add((-x, y))
#             result.add((-x, -y))
#     # print(result, len(result))
#     point_dict[radius] = len(result)
#     point_outline_dict[radius] = len(result_outline)
#     return len(result)


## v4
