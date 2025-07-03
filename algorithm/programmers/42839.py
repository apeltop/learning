# https://programmers.co.kr/learn/courses/30/lessons/42839
import itertools
from collections import defaultdict
from math import sqrt

prime_dict = defaultdict(bool)
def is_prime_number(x: int):
    if x == 0 or x == 1:
        return False

    for n in range(2, int(sqrt(x)) + 1):
        if x % n == 0:
            return False

    return True

def solution(numbers):
    answer = 0

    possibles = set()

    for i in range(1, len(numbers) + 1):
        for p in itertools.permutations(numbers, i):
            p = list(p)

            if p:
                possibles.add(int(''.join(p)))

    for p in possibles:
        if is_prime_number(p):
            answer += 1
    # print(possibles)
    return answer


# print(solution("17"))  # 3
# print(solution("011"))  # 2

print(solution("011"), 2)
print(solution("17"), 3)
