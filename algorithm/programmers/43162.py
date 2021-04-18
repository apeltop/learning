# https://programmers.co.kr/learn/courses/30/lessons/43162
import collections


def solution(n, computers):
    def dfs(s, index):
        visitDict[index] = True

        for i in range(len(computers)):
            if visitDict[i]:
                continue

            if computers[i][index] == 1:
                graph[s].append(i)
                dfs(s, i)

    graph = collections.defaultdict(list)
    visitDict = collections.defaultdict(bool)

    for i in range(len(computers)):
        if visitDict[i]:
            continue
        graph[i].append(i)
        dfs(i, i)

    return len(graph)


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
