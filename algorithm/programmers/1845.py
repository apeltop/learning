# https://school.programmers.co.kr/learn/courses/30/lessons/1845
from collections import defaultdict


def solution(nums):
    various_dict = defaultdict(int)

    for num in nums:
        various_dict[num] += 1

    return min(len(nums) // 2, len(various_dict))


print(solution([3, 1, 2, 3]), 2)
print(solution([3, 3, 3, 2, 2, 4]), 3)
print(solution([3, 3, 3, 2, 2, 2]), 2)
