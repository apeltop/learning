import copy
from collections import deque


def solution(n, info):
    answer = []

    def bfs():
        q = deque()
        q.append(([], n, 0, 0))
        cases = []

        while q:
            # print(q[0])
            scores, remain_n, index, current_score = q.popleft()
            if remain_n == 0:
                cases.append(scores)
                continue

            if remain_n and index == 10:
                scores.append(remain_n)
                cases.append(scores)
                continue

            zero_scores = scores[::]
            zero_scores.append(0)
            q.append((copy.copy(zero_scores), remain_n, index + 1, current_score))

            if info[index] == 0:
                scores.append(1)
                remain_n -= 1
            else:

                if info[index] + 1 <= remain_n:
                    scores.append(info[index] + 1)
                    remain_n -= info[index] + 1
                else:
                    continue

            q.append((copy.copy(scores), remain_n, index + 1, current_score + (10 - index)))

        return cases

    cases = bfs()
    max_diff_value = None
    max_diff_array = []
    for case in cases:
        case.extend([0 for i in range(11 - len(case))])

        peach_score, ryan_score = 0, 0
        for i, c in enumerate(case):
            if c < info[i]:
                peach_score += 10 - i
            elif c:
                ryan_score += 10 - i

        if ryan_score <= peach_score:
            continue

        if not max_diff_value:
            max_diff_value = ryan_score - peach_score
            max_diff_array = case

        elif max_diff_value < ryan_score - peach_score:
            max_diff_value = ryan_score - peach_score
            max_diff_array = case

        elif max_diff_value == ryan_score - peach_score:
            for i in range(10, 0, -1):
                if max_diff_array[i] < case[i]:
                    max_diff_array = case
                    break
                if max_diff_array[i] > case[i]:
                    break

    # print(max_diff_value)
    return max_diff_array if max_diff_array else [-1]


print(solution(10, [8, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]), [0, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0])

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]), [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [-1])
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]), [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0])
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]), [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2])
print(solution(2, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(solution(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]), [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0])
print(solution(10, [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]), [3, 3, 3, 0, 0, 1, 0, 0, 0, 0, 0])
print(solution(10, [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print(solution(3, [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), [-1])
print(solution(4, [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])
print(solution(5, [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]), [-1])
