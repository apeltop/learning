# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_d = deque()
    truck_d = deque(truck_weights)
    current_weight = 0

    if weight >= sum(truck_weights):
        return bridge_length + len(truck_weights)

    while truck_d:
        if weight >= current_weight + truck_d[0]:
            current_weight += truck_d[0]
            time = max(1, bridge_length - sum([elem[1] for elem in bridge_d]))
            bridge_d.append((truck_d.popleft(), time))
        else:
            current_weight -= bridge_d[0][0]
            answer += bridge_d.popleft()[1]

    while bridge_d:
        answer += bridge_d.popleft()[1]

    return answer + 1


print(solution(6, 10, [1]))  # 11
print(solution(6, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # 17
print(solution(6, 10, [7, 4, 5, 1, 3]))  # 19
print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(3, 7, [3, 4, 5]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
