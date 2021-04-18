import math


def solution(n, battery):
    answer = 0
    count = 0

    while count < n:
        biddingList = []
        for b in battery:
            biddingList.append((max(math.floor((n - count) / b[0]), 1) * b[1], b[0] * max((math.floor((n - count) / b[0]), 1))))

        b = min(biddingList)
        answer += b[0]
        count += b[1]

    return answer


print(solution(50, [[10, 100000], [4, 35000], [1, 15000]]))  # 450000
print(solution(20, [[6, 30000], [3, 18000], [4, 28000], [1, 9500]]))  # 108000
print(solution(5, [[2, 10], [1, 100], [2, 1500], [2, 1100]]))  # 30
print(solution(20, [[19, 30000], [3, 18000], [4, 28000], [1, 9500]]))  # 39500
print(solution(10, [[2, 900], [4, 1000], [2, 1500], [2, 1100]]))  # 2900
print(solution(10, [[4, 1000], [2, 1500], [2, 1100], [2, 900]]))  # 2900
print(solution(20, [[20, 3], [3, 18000], [4, 28000], [1, 9500]]))  # 3
print(solution(20, [[200, 3], [3, 18000], [4, 28000], [1, 9500]]))  # 3
print(solution(20, [[19, 30000], [3, 18000], [900, 100], [1, 9500]]))  # 100
