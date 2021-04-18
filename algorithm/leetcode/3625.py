# https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/

class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n))
        print(str(bin(n)).count('1'))
        return 0


print(Solution().hammingWeight(11))  # 3
