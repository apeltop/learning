import copy
from collections import defaultdict, deque


def solution(n, wires):
    answer = n
    wires.sort(reverse=True)

    wires_dict = defaultdict(int)
    for wire in wires:
        wires_dict[wire[0]] += 1
        wires_dict[wire[1]] += 1

    for wire in wires:
        if wires_dict[wire[0]] == 1:
            if n - 1 < answer:
                answer = n - 2
            continue
        if wires_dict[wire[1]] == 1:
            if n - 1 < answer:
                answer = n - 2
            continue

        exp_wires = wires[::-1]
        exp_wires.remove(wire)

        w1 = [wire[0]]
        w2 = [wire[1]]

        while len(w1) + len(w2) < n:
            for w in exp_wires:
                if w[0] in w1:
                    w1.extend(w)
                if w[1] in w1:
                    w1.extend(w)

                if w[0] in w2:
                    w2.extend(w)
                if w[1] in w2:
                    w2.extend(w)

                w1 = list(set(w1))
                w2 = list(set(w2))

        if len(w1) + len(w2) != n:
            continue

        if abs(len(w1) - len(w2)) < answer:
            answer = abs(len(w1) - len(w2))

    return answer


print(solution(3, [[2, 3], [1, 2]]), 1)
print(solution(8, [[1, 2], [1, 3], [1, 4], [4, 5], [5, 6], [6, 7], [6, 8]]), 0)
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]), 3)
print(solution(5, [[1, 2], [2, 3], [2, 4], [4, 5]]), 1)
print(solution(3, [[1, 2], [1, 3]]), 1)
print(solution(3, [[1, 2], [2, 3]]), 1)
print(solution(4, [[1, 2], [1, 3], [1, 4]]), 2)
print(solution(5, [[1, 2], [1, 3], [1, 4], [1, 5]]), 3)
print(solution(3, [[1, 2], [2, 3]]), 1)
print(solution(n=6, wires=[[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]), 2)
print(solution(4, [[1, 2], [3, 4], [2, 3]]), 0)
print(solution(3, [[1, 2], [2, 3]]), 1)
print(solution(2, [[1, 2], [1, 3]]), 0)
print(solution(4, [[1, 2], [1, 3], [1, 4]]), 2)
print(solution(10, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9], [9, 10]]), 2)
print(solution(11, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9], [9, 10], [0, 1]]), 3)
print(solution(4, [[1, 2], [2, 3], [3, 4]]), 0)
print(solution(6, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]), 0)
