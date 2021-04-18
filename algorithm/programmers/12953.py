# https://programmers.co.kr/learn/courses/30/lessons/12953
import math


def solution(arr):
    while len(arr) > 1:
        a, b = arr.pop(), arr.pop()
        arr.append(int(a * b / math.gcd(a, b)))
    return arr[0]


print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))  # 6
print(solution([10, 2, 3]))  # 30
