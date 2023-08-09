from math import floor, sqrt


def solution(k, d):
    answer = 0

    for v in range(0, d + 1, k):
        points = floor(sqrt(d ** 2 - v ** 2))
        answer += points // k + 1

    return answer


print(solution(1, 5), 26)
print(solution(2, 4), 6)
print(solution(1, 4), 17)
