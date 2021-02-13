# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1

        for a in arr:
            interval = a - num
            k -= interval
            if k < 1:
                return num + (k + interval - 1)

            num += 1 + interval

        return num - 1 + k


print(Solution().findKthPositive([2, 3, 4, 7, 11], 5))  # 9
print(Solution().findKthPositive([10], 5))  # 5
print(Solution().findKthPositive([1, 2, 3, 4], 2))  # 6
