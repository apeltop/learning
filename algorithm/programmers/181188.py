import collections


def solution(targets):
    answer = 0

    targets.sort(key=lambda x: (x[0], x[1]))

    targets = collections.deque(targets)

    l, r = targets.popleft()
    answer += 1

    while targets:
        target = targets.popleft()
        if l <= target[0] < r:
            r = min(target[1], r)
            continue

        l, r = target
        answer += 1

    return answer


print(solution([[3, 5], [3, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]), 2)  # 2
print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]), 3)  # 3
print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7]]), 2)  # 2
print(solution([[1, 2], [4, 5]]), 2)  # 2
print(solution([[4, 5], [1, 2]]), 2)  # 2
print(solution([[1, 5], [1, 2]]), 1)  # 1
print(solution([[1, 2], [1, 2]]), 1)  # 1
print(solution([[3, 6], [2, 4], [5, 6], [1, 3]]), 2)  # 1
print(solution([[4, 5], [4, 8]]), 1)  # 1
print(solution([[4, 5], [4, 5]]), 1)  # 1
print(solution([[4, 5], [3, 4]]), 2)  # 1
print(solution([[1, 4], [1, 2], [2, 3]]), 2)  # 1
