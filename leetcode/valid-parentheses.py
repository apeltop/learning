# https://leetcode.com/problems/valid-parentheses/
# 파이썬 알고리즘 인터뷰 책 참고 p.245

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0


print(Solution().isValid(s="()"))  # True
print(Solution().isValid(s="()[]{}"))  # True
print(Solution().isValid(s="(]"))  # False
print(Solution().isValid(s="([)]"))  # False
print(Solution().isValid(s="{[]}"))  # True
