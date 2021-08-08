# https://leetcode.com/problems/reverse-string/
from typing import List


# Runtime: 192 ms, faster than 88.79% of Python3 online submissions for Reverse String.
# Memory Usage: 18.6 MB, less than 43.53% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(int(len(s) / 2)):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


print(Solution().reverseString(s=["h", "e", "l", "l", "o"]))  # ["o","l","l","e","h"]
print(Solution().reverseString(s=["H", "a", "n", "n", "a", "h"]))  # ["h","a","n","n","a","H"]
