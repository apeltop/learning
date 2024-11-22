# https://leetcode.com/problems/container-with-most-water/description/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_i, r_i = 0, len(height) - 1

        max_value = (r_i - l_i) * min(height[l_i], height[r_i])

        while l_i < r_i:
            if height[l_i] < height[r_i]:
                l_i += 1
            else:
                r_i -= 1
            max_value = max(max_value, (r_i - l_i) * min(height[l_i], height[r_i]))

        return max_value


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
