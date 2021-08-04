# https://leetcode.com/problems/valid-palindrome/
import re
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Runtime: 48 ms, faster than 62.01% of Python3 online submissions for Valid Palindrome.
        #Memory Usage: 14.4 MB, less than 99.12% of Python3 online submissions for Valid Palindrome.
        strs = ""

        for i in range(len(s)):
            if s[i].isalnum():
                strs += s[i]

        strs = strs.lower()
        return strs == strs[::-1]

        #Runtime: 56 ms
        #Memory Usage: 19.3 MB
        # strs = deque()
        #
        # for c in s:
        #     if c.isalnum():
        #         strs.append(c.lower())
        #
        # while len(strs) > 1:
        #     if strs.popleft() != strs.pop():
        #         return False
        #
        # return True

        # Runtime: 48 ms
        # Memory Usage: 20.2 MB
        # strs = []
        #
        # for c in s:
        #     if c.isdecimal():
        #         strs.append(c)
        #     if c.isalnum():
        #         strs.append(c.lower())
        #
        # return strs == strs[::-1]


print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))  # true
print(Solution().isPalindrome(s="race a car"))  # false
