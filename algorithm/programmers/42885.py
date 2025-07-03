# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque


def solution(people, limit):
    answer = 0

    people.sort()

    l_i = 0
    r_i = len(people) - 1

    while l_i < r_i:
        if people[l_i] + people[r_i] <= limit:
            answer += 1
            l_i += 1
            r_i -= 1
            continue

        r_i -= 1
        answer += 1

    if l_i == r_i:
        answer += 1

    return answer

print(solution([20, 60, 70, 80, 30], 100), 3)

print(solution([99, 99, 59, 40], 100), 3)
print(solution([51, 51], 51), 2)
print(solution([51, 51], 100), 2)
print(solution([1, 49, 1, 48, 48], 100), 3)
print(solution([1, 49, 1, 48, 100], 100), 3)
print(solution([1, 49, 1, 48, 1], 100), 3)
print(solution([1, 49, 1, 49, 100], 100), 3)
print(solution([100, 100, 100, 100, 100], 100), 5)
print(solution([100, 100, 100, 100], 100), 4)
print(solution([1, 1, 1, 1], 1), 4)
print(solution([50, 50, 50, 51], 100), 3)
print(solution([50, 100, 50, 51], 100), 3)
print(solution([50, 50, 50, 50], 100), 2)
print(solution([1, 1, 1, 1, 1], 100), 3)
print(solution([70, 50, 80, 49], 100), 3)
print(solution([70, 50, 80, 50], 100), 3)
print(solution([70, 80, 50], 100), 3)
print(solution([1, 1, 1], 100), 2)
print(solution([1, 1], 100), 1)
print(solution([100, 1], 100), 2)
print(solution([100, 100], 100), 2)
print(solution([99, 99, 99], 100), 3)
print(solution([99, 99, 99, 2], 100), 4)
print(solution([240], 240), 1)
print(solution([40, 40], 240), 1)
print(solution([40, 40, 240], 240), 2)
print(solution([40, 40, 200, 240], 240), 3)
print(solution([40, 40, 200, 200, 240], 240), 3)
print(solution([39, 39, 199, 199, 239], 240), 3)
print(solution([39, 39, 199, 199, 239, 1], 240), 3)
print(solution([39, 39, 199, 199, 239, 2], 240), 4)

print(solution([i for i in range(50000)], 100), 3)
print(solution([1 for i in range(25000)] + [100 for i in range(25000)], 100), 3)

