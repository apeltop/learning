from collections import deque
from copy import deepcopy


def solution(storey):
    answer = 0
    q = deque([(storey, 0, 1)])

    def find_least_stone():
        least_count = None
        while q:
            s, history_count, index = q.popleft()
            if s == 0:
                if not least_count or history_count < least_count:
                    least_count = history_count
                    continue

            if least_count is not None and history_count >= least_count:
                continue

            current_unit = int(str(s)[-index])
            current_value = int(str(s)[-index:])

            if current_unit == 0:
                q.append((s, history_count, index + 1))
                continue

            increment_size1 = 10 - current_unit
            increment_value1 = increment_size1 * (10 ** (index - 1)) if current_value >= 10 else increment_size1
            q.append((s + increment_value1, history_count + increment_size1, index + 1))

            increment_size2 = current_unit
            increment_value2 = increment_size2 * (10 ** (index - 1)) if current_value >= 10 else increment_size2
            q.append((s - increment_value2, history_count + increment_size2, index + 1))
        return least_count

    return find_least_stone()


def solution2(storey):
    answer = 0

    index = 1
    while storey != 0:
        current_unit = int(str(storey)[-index])
        current_value = int(str(storey)[-index:])

        if current_unit != 0:
            increment_size = 10 - current_unit if current_unit > 5 else current_unit
            increment_value = increment_size * (10 ** (index - 1)) if current_value >= 10 else increment_size
            storey += increment_value if current_unit > 5 else -increment_value

            answer += increment_size
        index += 1

    return answer


print(solution(9975), solution2(9975), 8)
print(solution(9995), solution2(9995), 6)
# print(solution(1991), solution2(1991), 4)
# print(solution(1991), solution2(1991), 4)
# print(solution(1), solution2(1), 1)
# print(solution(16), solution2(16), 6)
# print(solution(10), solution2(10), 1)
# print(solution(100), solution2(100), 1)
# print(solution(101), solution2(101), 2)
# print(solution(111), solution2(111), 3)
# print(solution(166), solution2(166), 9)
# print(solution(999), solution2(999), 2)
# print(solution(1001), solution2(1001), 2)
# print(solution(2554), solution2(2554), 16)

# for i in range(10000):
#     print(i, solution(i), solution2(i))
