# https://programmers.co.kr/learn/courses/30/lessons/49189
import collections
import heapq


def solution(n, edge):
    graph = collections.defaultdict(list)

    for u, v in edge:
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    Q = [(0, 1)]
    dist = collections.defaultdict(int)

    while Q:
        t, n = heapq.heappop(Q)

        if n not in dist:
            dist[n] = t
            for v, w in graph[n]:
                heapq.heappush(Q, (t + w, v))

    return list(dist.values()).count(max(dist.values()))


print(solution(6, [[3, 6], [4, 3], [3, 7], [1, 3], [1, 7], [7, 4], [5, 7]]))  # 3
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [7, 5]]))  # 1
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [8, 9]]))  # 2
print(solution(6, [[2, 1]]))  # 3
