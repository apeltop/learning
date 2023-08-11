import math
from functools import reduce


def find_gcd(list):
    x = reduce(math.gcd, list)
    return x

def solution(arrayA, arrayB):
    answer = 0

    # gcd_a = math.gcd(*arrayA)
    gcd_a = find_gcd(arrayA)
    gcd_b = find_gcd(arrayB)

    if gcd_a == 1 and gcd_b == 1:
        return 0

    has_divide_b = False
    has_divide_a = False

    for b in arrayB:
        if b % gcd_a == 0:
            has_divide_b = True
            break

    for a in arrayA:
        if a % gcd_b == 0:
            has_divide_a = True
            break

    if not has_divide_b and not has_divide_a:
        return max(gcd_a, gcd_b)

    if not has_divide_b:
        return gcd_a

    if not has_divide_a:
        return gcd_b

    return answer


print(solution([3], [7]), 7)

print(solution([10, 20], [5, 17]), 10)

print(solution([10, 17], [5, 17]), 0)
print(solution([10, 17], [5, 20]), 0)

print(solution([5, 17], [10, 20]), 10)

print(solution([14, 35, 119], [18, 30, 102]), 7)
print(solution([1], [1]), 0)
print(solution([3], [2]), 3)
print(solution([7 for _ in range(500000)], [18, 30, 102]), 7)
