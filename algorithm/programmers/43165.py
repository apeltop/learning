# https://programmers.co.kr/learn/courses/30/lessons/43165
import collections


def solution(numbers, target):
    def dfs(next_elem):
        if not next_elem:
            dic[''.join([str(e) for e in prev_elem[:]])] = True
            if sum(prev_elem) == target:
                answer[''.join([str(e) for e in prev_elem[:]])] = True

        for elem in next_elem:
            prev_elem.append(elem)
            next_e = next_elem[:]
            next_e.remove(elem)

            if ''.join([str(e) for e in prev_elem[:]]) in dic:
                prev_elem.pop()
                continue
            dfs(next_e)
            prev_elem.append(-prev_elem.pop())
            dfs(next_e)
            prev_elem.pop()

    answer = collections.defaultdict(bool)
    dic = {}
    prev_elem = []
    dfs(numbers)
    return len(answer)


# print(*itertools.permutations([1,2,3], 3))
# print(*itertools.combinations([1,2,3], 3))
# print(solution([1, 2, 3], 6))  # 1
print(solution([1, 1, 1, 1, 1], 3))  # 5
