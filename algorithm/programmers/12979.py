from math import ceil


def solution(n, stations, w):
    answer = 0
    current_index = 1

    for i, station in enumerate(stations):
        prev_end_point = stations[i - 1] + w + 1 if i != 0 else 1
        answer += ceil((station - w - prev_end_point) / ((w * 2) + 1))

        current_index = station + w

    if current_index < n:
        prev_end_point = current_index
        answer += ceil((n - prev_end_point) / ((w * 2) + 1))

    return answer


print(solution(11, [1, 4, 7, 10], 1), 0)
print(solution(11, [11], 1), 3)

print(solution(11, [1, 2], 1), 3)
print(solution(11, [1], 1), 3)

print(solution(11, [4, 11, ], 1), 3)
print(solution(16, [9, ], 2), 3)
