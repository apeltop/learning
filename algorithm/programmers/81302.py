from itertools import combinations


def calc_l1_distance(yx1, yx2):
    return abs(yx1[1] - yx2[1]) + abs(yx1[0] - yx2[0])


def solution(places):
    answer = []

    for place in places:
        is_pass = True

        p_yx_list = []
        for y, row in enumerate(place):
            for x, col in enumerate(row):
                if place[y][x] == 'P':
                    p_yx_list.append((y, x))

        l1_1distance_case = [case for case in list(combinations(p_yx_list, 2)) if calc_l1_distance(case[0], case[1]) == 1]
        if any(l1_1distance_case):
            is_pass = False

        l1_2distance_case = [case for case in list(combinations(p_yx_list, 2)) if calc_l1_distance(case[0], case[1]) == 2]
        for case in l1_2distance_case:
            yx1, yx2 = case
            bound_yx1 = (min(yx1[0], yx2[0]), min(yx1[1], yx2[1]))
            bound_yx2 = (max(yx1[0], yx2[0]), max(yx1[1], yx2[1]))

            bound_1d = []
            for y in range(bound_yx1[0], bound_yx2[0] + 1):
                for x in range(bound_yx1[1], bound_yx2[1] + 1):
                    bound_1d.append(place[y][x])

            if any([bound == 'O' for bound in bound_1d]):
                is_pass = False
                break

        answer.append(1 if is_pass else 0)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
                ]))  # [1, 0, 1, 1, 1]

print(solution([
                ["PPPPP", "PPPPP", "PPPPP", "PPPPP", "PPPPP"],
                ]))  # [0]