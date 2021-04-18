# product-of-array-except-self
# 파이썬 알고리즘 인터뷰 책 참고 p.193
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1

        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out


print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
