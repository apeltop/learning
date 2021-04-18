# https://leetcode.com/problems/two-sum/
# 파이썬 알고리즘 인터뷰 책 참고 p.173
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
print(Solution().twoSum(nums=[3, 2, 4], target=6))  # [1, 2]
print(Solution().twoSum(nums=[3, 3], target=6))  # [0, 1]
