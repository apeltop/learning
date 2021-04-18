# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            if i == 0:
                continue
            else:
                nums[i] = nums[i - 1] + nums[i]
        return nums


print(Solution().runningSum([1, 2, 3, 4]))  # [1,3,6,10]
print(Solution().runningSum([1, 1, 1, 1, 1]))  # [1,2,3,4,5]
print(Solution().runningSum([3, 1, 2, 10, 1]))  # [3,4,6,16,17]
