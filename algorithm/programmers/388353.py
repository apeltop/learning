# https://school.programmers.co.kr/learn/courses/30/lessons/388353
from collections import defaultdict


def solution(storage, requests):
    def is_valid_yx(y, x):
        return 0 <= y < len(storage) or 0 <= x < len(storage[0])

    answer = len(storage) * len(storage[0])

    for y in range(len(storage)):
        storage[y] = [''] + [a for a in storage[y]] + ['']

    storage.insert(0, ['' for _ in storage[0]])
    storage.append(['' for _ in storage[0]])

    available_storages = defaultdict(set)
    for y in range(len(storage)):
        for x in range(len(storage[0])):
            if (y == 1 or y == len(storage) - 2) or (x == 1 or x == len(storage[0]) - 2):
                available_storages[storage[y][x]].add((y, x))

    for req in requests:
        def explore_available_storage(yx):
            y, x = yx[0], yx[1]
            is_able = False
            explore_yx, pop_yx = {(y, x)}, {(y, x)}
            possible_yx, visit_yx = set(), set()

            while explore_yx:
                ey1, ex1 = explore_yx.pop()

                for py1, px1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    y2, x2 = ey1 + py1, ex1 + px1
                    if not is_valid_yx(y2, x2) or (y2, x2) in visit_yx:
                        continue

                    is_able = True if is_able else storage[y2][x2] == ''

                    if storage[y2][x2] == 'POP':
                        explore_yx.add((y2, x2))
                        pop_yx.add((y2, x2))

                        if len(req) == 1:
                            storage[y2][x2] = ''
                    else:
                        possible_yx.add((y2, x2))

                        if len(req) == 1:
                            available_storages[storage[y2][x2]].add((y2, x2))

                    visit_yx.add((y2, x2))
            if is_able:
                for yx in pop_yx:
                    storage[yx[0]][yx[1]] = ''
                for yx in possible_yx:
                    available_storages[storage[yx[0]][yx[1]]].add((yx[0], yx[1]))

        if len(req) == 1:
            if req not in available_storages:
                continue

            for y1, x1 in available_storages[req].copy():
                if storage[y1][x1] == '':
                    continue

                answer -= 1
                storage[y1][x1] = ''
                explore_available_storage((y1, x1))
        else:
            for y in range(len(storage)):
                for x in range(len(storage[0])):
                    if storage[y][x] != req[0]:
                        continue

                    answer -= 1
                    storage[y][x] = 'POP'
                    explore_available_storage((y, x))

    return answer


print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["DD", "CC", "A"]), 8)

print(solution([
    ''.join(['A' for _ in range(50)]),
    ''.join(['B' for _ in range(50)]),
    ''.join(['C' for _ in range(50)]),
    ''.join(['D' for _ in range(50)]),
    ''.join(['E' for _ in range(50)]),
    ''.join(['F' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['H' for _ in range(50)]),
    ''.join(['I' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['A' for _ in range(50)]),
    ''.join(['B' for _ in range(50)]),
    ''.join(['C' for _ in range(50)]),
    ''.join(['D' for _ in range(50)]),
    ''.join(['E' for _ in range(50)]),
    ''.join(['F' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['H' for _ in range(50)]),
    ''.join(['I' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['A' for _ in range(50)]),
    ''.join(['B' for _ in range(50)]),
    ''.join(['C' for _ in range(50)]),
    ''.join(['D' for _ in range(50)]),
    ''.join(['E' for _ in range(50)]),
    ''.join(['F' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['H' for _ in range(50)]),
    ''.join(['I' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['A' for _ in range(50)]),
    ''.join(['B' for _ in range(50)]),
    ''.join(['C' for _ in range(50)]),
    ''.join(['D' for _ in range(50)]),
    ''.join(['E' for _ in range(50)]),
    ''.join(['F' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['H' for _ in range(50)]),
    ''.join(['I' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['A' for _ in range(50)]),
    ''.join(['B' for _ in range(50)]),
    ''.join(['C' for _ in range(50)]),
    ''.join(['D' for _ in range(50)]),
    ''.join(['E' for _ in range(50)]),
    ''.join(['F' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
    ''.join(['H' for _ in range(50)]),
    ''.join(['I' for _ in range(50)]),
    ''.join(['G' for _ in range(50)]),
], ["B", "A", 'B', 'I', 'A', 'A', 'A', 'B', 'II']), 2086)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["A", "A", 'A']), 0)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["B"]), 250)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["B", "A"]), 144)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["A", "B"]), 144)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["B", "A"]), 144)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["AA", "AA"]), 0)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["BB", "AA"]), 0)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["BB", "BB"]), 250)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["AA", "BB", "A"]), 0)

print(solution([''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]), ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)]),
                ''.join(['A' for _ in range(50)])], ["A", "BB", "A"]), 46)

print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]), 11)
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]), 4)
print(solution(["AA"], ["A", "BB", "A"]), 0)
print(solution(["CC"], ["A", "BB", "A"]), 2)
print(solution(["D"], ["A", "BB", "A"]), 1)
print(solution(["ABABABABABA"], ["A", "BB", "A"]), 0)
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["Y", "BB", "A"]), 10)
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["Y", "CC", "A"]), 10)
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["D", "CC", "A"]), 11)
