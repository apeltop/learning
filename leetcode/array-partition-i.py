# https://leetcode.com/problems/array-partition-i/
# 파이썬 알고리즘 인터뷰 책 참고 p.190
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


print(Solution().arrayPairSum([1, 4, 3, 2]))  # 4
print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))  # 9
