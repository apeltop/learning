def solution(diffs, times, limit):
    answer = 0

    def calc_time(level):
        # print()
        total_spend_time = 0
        for i, diff in enumerate(diffs):
            if diff <= level:
                total_spend_time += times[i]
                continue

            total_spend_time += (times[i - 1] + times[i]) * (diff - level) + times[i]

        # print(level, total_spend_time, limit)
        return total_spend_time <= limit

    i = 0
    start_pos = 0
    end_pos = max(diffs)
    while end_pos - start_pos > 100:
        mid = int((start_pos + end_pos) / 2)
        if calc_time(mid):
            end_pos = mid
        else:
            start_pos = mid

    if start_pos == 0:
        start_pos = 1
    for i in range(start_pos, end_pos + 1):
        if calc_time(i):
            return i

    return answer


print(solution([4, 4, 4, 4], [1, 1, 1, 1], 59), 1)
print(solution([i for i in range(1, 1000 + 1)], [1 for i in range(1000)], 1000000), 1)
print(solution([i for i in range(1000)], [1 for i in range(1000)], 1723), 294)
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012), 39354)
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59), 2)
print(solution([1, 5, 3], [2, 4, 7], 30), 3)
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723), 294)
