# https://programmers.co.kr/learn/courses/30/lessons/42890
import itertools


def solution(relation):
    answer = 0
    i = 1
    columns = (list(zip(*relation)))
    while i <= len(columns):
        keys = []
        for e in itertools.combinations(columns, i):
            s = set()
            for a in list(zip(*e)):
                s.add(a)
            if len(s) == len(e[0]):
                keys.append(e)
                answer += 1
        while keys:
            for key in keys.pop():
                if key in columns:
                    columns.remove(key)
        i += 1

    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))  # 2

print(solution([["a", "aa"],
                ["aa", "a"],
                ["a", "a"]]))  # 1

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "1"]]))  # 4


print(solution([["100", "ryan", "music", "2"]]))  # 4


print(solution(
    [['a', '1', '4'],
     ['2', '1', '5'],
     ['a', '2', '4']]))  # 2


print(solution(
    [['a', 'a', 'c'],
     ['a', 'b', 'b'],
     ['c', 'c', 'c']]))  # 1

print(solution(
    [['b', '2', 'a', 'a', 'b'],
     ['b', '2', '7', '1', 'b'],
     ['1', '0', 'a', 'a', '8'],
     ['7', '5', 'a', 'a', '9'],
     ['3', '0', 'a', 'f', '9']]))  # 5
# (('b', 'b', '1', '7', '3'), ('a', '7', 'a', 'a', 'a'))
# (('b', 'b', '1', '7', '3'), ('a', '1', 'a', 'a', 'f'))
# (('2', '2', '0', '5', '0'), ('a', '1', 'a', 'a', 'f'))
# (('a', '1', 'a', 'a', 'f'), ('b', 'b', '8', '9', '9'))





print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "math", "2"]]))  # 1
