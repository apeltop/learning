# https://programmers.co.kr/learn/courses/30/lessons/64062
import collections


def solution(stones, k):
    answer = max(stones[0:k])

    i = k
    while i < len(stones) - k:
        answer = min(answer, max(stones[i:i+k]))
        i += 1

    return answer


print(solution([1], 3))  # 3
print(solution([1, 2], 3))  # 3
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))  # 3
print(solution([2, 4, 5, 7, 2, 1, 4, 2, 5, 1], 3))  # 4
# print(sorted(collections.Counter([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]).most_common())[3 - 1][0])

# def solution(stones, k):
#     answer = 200000001
#     i = 0
#
#     while i < len(stones) - k:
#         max_n = max(stones[i:i+k])
#         if answer > max_n:
#             answer = max_n
#         i += 1
#
#     return answer
