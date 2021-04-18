# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[-1]
        while len(nums) != 1:
            a = nums.pop()
            b = nums.pop()
            s = a + b

            if max_num < a:
                max_num = a
            if s > max_num:
                max_num = s
            if s < 1 or a < 0:
                nums.append(b)
                continue

            nums.append(s)

        return max_num if nums[0] < max_num else nums[0]


print(Solution().maxSubArray([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]) == 187)  # 187
print(Solution().maxSubArray([-1, 0, -2]) == 0)
print(Solution().maxSubArray([1, 1, 1, -1]) == 3)
print(Solution().maxSubArray([-1, -2]) == -1)
print(Solution().maxSubArray([10, 1, -1, 1]) == 11)
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 10]) == 11)
print(Solution().maxSubArray([1]) == 1)
print(Solution().maxSubArray([0]) == 0)
print(Solution().maxSubArray([-1]) == -1)
print(Solution().maxSubArray([-2147483647]) == -2147483647)
