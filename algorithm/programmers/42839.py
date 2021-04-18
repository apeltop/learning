# https://programmers.co.kr/learn/courses/30/lessons/42839
import itertools


def solution(numbers):
    def permutation(elements):
        if not elements:
            answer.append(prev_elem[:])

        for elem in elements:
            prev_elem.append(elem)
            nextElem = next_elem[:]
            nextElem = nextElem.replace(elem, '', 1)

            permutation(nextElem)

            prev_elem.pop()

    answer = []

    prev_elem = []
    next_elem = numbers[:]

    permutation(numbers)

    return answer


print('11'.replace('1', '2', 1))

print(solution("17"))  # 3
print(solution("011"))  # 2

print(*itertools.permutations("011", 2))
print(*itertools.permutations("011", 3))
