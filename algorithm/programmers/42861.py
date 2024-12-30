# https://school.programmers.co.kr/learn/courses/30/lessons/42861
from collections import defaultdict


def solution(n, costs):
    answer = 0
    island_maps = defaultdict(list)
    island_wait_map = [i for i in range(n)]

    for cost in costs:
        t1, t2, c = cost

        island_maps[t1].append((c, t2))
        island_maps[t2].append((c, t1))

    candidate = island_maps[island_wait_map.pop()]
    while island_wait_map:
        candidate = sorted(candidate, reverse=True)

        c, t2 = candidate.pop()
        if t2 not in island_wait_map:
            continue

        candidate.extend(island_maps[t2])
        island_wait_map.remove(t2)
        answer += c

    return answer


print(solution(4, [[1, 0, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 4)
print(solution(4, [[0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 8)
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 4)
