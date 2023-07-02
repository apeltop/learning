# https://school.programmers.co.kr/learn/courses/30/lessons/154538
from collections import deque


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def solution(x, y, n):
    if x == y:
        return 0

    def min_calc():
        q = deque()
        q.append((y, '/2', 1))
        q.append((y, '/3', 1))
        q.append((y, '+N', 1))

        while q:
            num, command, count = q.popleft()
            if command == '/2':
                num /= 2
            if command == '/3':
                num /= 3
            if command == '+N':
                num -= n

            if not is_integer(num):
                continue

            if num < x:
                continue

            if num == x:
                return count

            q.append((num, '/2', count + 1))
            q.append((num, '/3', count + 1))
            q.append((num, '+N', count + 1))

        return -1

    answer = min_calc()

    return answer


print(solution(3, 3, 1), 0)  #
print(solution(3, 9, 8), 1)  #
print(solution(1, 9, 8), 1)  #
print(solution(1, 9, 1), 2)  #
print(solution(1, 2, 1), 1)  #
print(solution(1, 3, 1), 1)  #
print(solution(1, 4, 2), 2)  #
print(solution(1, 4, 3), 1)  #
print(solution(1, 10, 1), 3)  #

print(solution(1, 1000000, 1), 19)  #

print(solution(1, 5, 1), 3)  # 3
print(solution(10, 40, 5), 2)  # 2
print(solution(10, 40, 30), 1)  # 1
print(solution(2, 5, 4), -1)  # -1
