# https://leetcode.com/problems/jewels-and-stones/
import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        countStone = collections.Counter(stones)

        total = 0
        for j in jewels:
            total += countStone[j]

        return total


print(Solution().numJewelsInStones(jewels="aA", stones="aAAbbbb"))  # 3
print(Solution().numJewelsInStones(jewels="z", stones="ZZ"))  # 0
