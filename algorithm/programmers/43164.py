# https://programmers.co.kr/learn/courses/30/lessons/43164
import collections


def solution(tickets):
    answer = []
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    def dfs(city):
        while graph[city]:
            dfs(graph[city].pop(0))
        answer.append(city)

    dfs('ICN')

    return answer[::-1]


# print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))  # [ICN, JFK, HND, IAD]
print(solution(
    [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))  # [ICN, ATL, ICN, SFO, ATL, SFO]
