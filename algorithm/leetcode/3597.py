# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


print(Solution().arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))  # false
print(Solution().arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))  # true
