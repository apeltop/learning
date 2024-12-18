def solution(numbers):
    return [n + ((n ^ n + 1) >> 2) + 1 for n in numbers]


print(solution([2, 7]), [3, 11])  # [3, 11]
print(solution([1]), [2])  # [2]
# print(solution([i for i in range(100000)]))
# solution([10 ** 15 - i * 5 for i in range(100000)])
# print(solution([10 ** 15 - i * 5 for i in range(100000)]))  # [2]
