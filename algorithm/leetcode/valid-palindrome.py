# https://leetcode.com/problems/valid-palindrome/
import re

# 파이썬 알고리즘 인터뷰 책 참고 p.141
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))  # True
print(Solution().isPalindrome("race a car"))  # False
