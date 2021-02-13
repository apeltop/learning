# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
import collections


class Solution:
    def isHappy(self, n: int) -> bool:
        dic = collections.defaultdict(bool)

        while n != 1:
            n = sum([int(a) ** 2 for a in str(n)])
            if n in dic:
                return False
            dic[n] = True

        return True


print(Solution().isHappy(7))
print(Solution().isHappy(19))
print(Solution().isHappy(2))
