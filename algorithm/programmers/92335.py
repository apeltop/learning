import math
import re
from collections import deque


def ternary(n, k):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, k)
        nums.append(str(r))
    return ''.join(reversed(nums))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    primes = []
    zeros = deque([])

    n = ternary(n, k)

    for r in re.finditer('0', n):
        index = r.span()
        zeros.append(index[0])

    if not zeros:
        return 1 if is_prime(int(n)) else 0

    if n[0] != '0':
        primes.append(n[0:zeros[0]])
        # zeros.popleft()
    if n[len(n) - 1] != '0':
        primes.append(n[zeros[-1] + 1::])

    while len(zeros) > 1:
        primes.append(n[zeros[0] + 1:zeros[1]])
        zeros.popleft()

    for prime in primes:
        if prime and is_prime(int(prime)):
            answer += 1

    return answer


print(solution(437674, 3), 3)
print(solution(110011, 10), 2)
print(solution(12, 10), 0)
print(solution(00, 10), 0)
print(solution(10, 10), 0)
print(solution(20, 10), 1)
print(solution(2, 10), 1)
print(solution(1, 10), 0)
print(solution(8, 10), 0)
print(solution(3170, 10), 1)
print(solution(30, 10), 1)
print(solution(30, 10), 1)
print(solution(37, 10), 1)
print(solution(370, 10), 1)
print(solution(20370, 10), 2)
print(solution(202037, 10), 3)
print(solution(370160, 10), 1)
print(solution(37017, 10), 2)
print(solution(3702017, 10), 3)
print(solution(37020017, 10), 3)
print(solution(3700200017, 10), 3)
