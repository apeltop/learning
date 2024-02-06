from collections import deque, defaultdict


def solution(k, n, reqs):
    answer = 0

    min_wait_time = None
    reqs_by_kind_dict = defaultdict(list)
    for req in reqs:
        reqs_by_kind_dict[req[2]].append(req)

    def calc_wait_time(kind, mentor_n):
        waiting_time = 0
        reqs_by_kind = deque(reqs_by_kind_dict[kind])
        if not reqs_by_kind:
            return 0

        q = deque([])

        while reqs_by_kind:
            req = reqs_by_kind.popleft()

            if len(q) < mentor_n:
                q.append(req[0] + req[1])
                continue

            q = sorted(q, reverse=True)
            cur_time = max(q[-1], req[0])
            waiting_time += max(cur_time - req[0], 0)

            q.pop()
            q.append(cur_time + req[1])

        return waiting_time

    mentor_dict = {kind + 1: 1 for kind in range(k)}

    if sum(mentor_dict.values()) == n:
        wait_time_dict = {k: calc_wait_time(k, v) for k, v in mentor_dict.items()}
        return sum([v for v in wait_time_dict.values()])

    while sum(mentor_dict.values()) < n:
        wait_time_possible_dict = defaultdict(int)
        for i in range(1, k + 1):
            mentor_copy = mentor_dict.copy()
            mentor_copy[i] += 1
            wait_time_dict = {k: calc_wait_time(k, v) for k, v in mentor_copy.items()}

            wait_time_possible_dict[i] = sum([v for v in wait_time_dict.values()])

        mentor_key = sorted([v for v in wait_time_possible_dict.items()], key=lambda x: x[1])[0][0]

        if min_wait_time is None:
            min_wait_time = wait_time_possible_dict[mentor_key]
        elif min_wait_time > wait_time_possible_dict[mentor_key]:
            min_wait_time = wait_time_possible_dict[mentor_key]

        mentor_dict[mentor_key] += 1
    return min_wait_time


print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]), 90)

print(solution(3, 3, [[0, 5, 1], [19, 5, 2], [20, 15, 3], [30, 40, 2], [30, 40, 1]]), 0)
print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1],
                      [70, 100, 2]]), 25)
print(solution(2, 3, [[0, 100, 1], [5, 100, 2], [10, 100, 1], [15, 30, 2], [20, 100, 1], [45, 10, 2], [60, 5, 2]]), 270)
print(solution(2, 2, [[0, 5, 1], [19, 5, 2], [20, 15, 2], [30, 40, 2], [30, 40, 1]]), 13)
print(solution(2, 2, [[0, 5, 1], [10, 5, 2], [20, 15, 2], [30, 40, 2], [30, 40, 1]]), 5)
print(solution(2, 2, [[0, 5, 2], [10, 5, 2], [20, 15, 2], [30, 40, 1]]), 0)
print(solution(2, 2, [[0, 5, 2], [10, 5, 2], [20, 15, 2], [30, 40, 2]]), 5)
print(solution(2, 2, [[0, 5, 2], [10, 5, 2], [20, 11, 2], [30, 40, 2]]), 1)
print(solution(2, 2, [[5, 5, 2], [10, 5, 2], [20, 11, 2], [30, 40, 2]]), 1)
print(solution(2, 3, [[5, 5, 2], [10, 5, 2], [20, 11, 2], [30, 40, 2]]), 0)
print(solution(2, 3, [[5, 5, 2], [10, 5, 2], [20, 5, 2]]), 0)
print(solution(2, 3, [[5, 5, 2], [10, 5, 2], [20, 5, 2], [30, 40, 2]]), 0)
print(solution(2, 3, [[5, 5, 2], [10, 5, 2], [20, 10, 2], [30, 40, 2]]), 0)
