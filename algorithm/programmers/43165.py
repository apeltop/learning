# https://programmers.co.kr/learn/courses/30/lessons/43165
import collections
from itertools import product


def solution(numbers, target):
    def bfs():
        q = collections.deque([[numbers[0]], [-numbers[0]]])
        possible = []

        while q:
            arr = q.popleft()

            if len(arr) == len(numbers):
                if sum(arr) == target:
                    possible.append(arr)
                continue

            q.append(arr + [numbers[len(arr)]])
            q.append(arr + [-numbers[len(arr)]])

        return possible

    return len(bfs())

# print(list(product(*[(x, -x) for x in [1, 2, 3]])))
print(solution([1, 2, 3], 6), 1)  # 1
print(solution([1, 1, 1, 1, 1], 3), 5)  # 5
print(solution([4, 1, 2, 1], 4), 2)  # 5
