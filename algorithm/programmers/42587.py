# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = 0

    priorities_d = deque(priorities)
    while priorities_d:
        j = priorities_d.popleft()
        if priorities_d and j < max(priorities_d):
            priorities_d.append(j)
            if location == 0:
                location += len(priorities_d)
        else:
            answer += 1
            if location == 0:
                break

        location -= 1

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
print(solution([2, 1, 9, 2, 2, 2], 1))  # 6
print(solution([1, 1, 1, 1, 1, 1], 0))  # 1
print(solution([1, 1, 1, 1, 1, 2], 0))  # 2
print(solution([2, 1, 3, 2], 2))  # 1
print(solution([2, 1, 3, 2], 1))  # 4
print(solution([2, 1, 9, 2, 1, 1], 0))  # 3
print(solution([1, 1, 9, 1, 1, 1], 2))  # 1
