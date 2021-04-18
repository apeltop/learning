# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        while nums:
            if i == len(nums) - 1:
                return nums[i]
            elif nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]


print(Solution().singleNumber([2, 2, 1]))  # 1
print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 4
print(Solution().singleNumber([1]))  # 1
