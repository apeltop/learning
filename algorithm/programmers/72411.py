from collections import defaultdict, Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    comb_dict = defaultdict(list)
    for cor in course:
        for order in orders:
            comb_dict[cor].extend(map(lambda x: ''.join(sorted(x)), (combinations(order, r=cor))))

        if len(comb_dict[cor]) < 2:
            continue

        counter = Counter(comb_dict[cor])
        most = counter.most_common()
        answer += [k for k, v in most if v > 1 and v == most[0][1]]

    return sorted(answer)


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]), ["WX", "XY"])
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]), ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]), ["ACD", "AD", "ADE", "CD", "XYZ"])
