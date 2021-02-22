# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 파이썬 알고리즘 인터뷰 책 참고 p.195
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
