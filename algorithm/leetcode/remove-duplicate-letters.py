# https://leetcode.com/problems/remove-duplicate-letters/
# 파이썬 알고리즘 인터뷰 책 참고 p.247
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


print(Solution().removeDuplicateLetters("cbacdcbc"))  # acdb
print(Solution().removeDuplicateLetters("bcabc"))  # abc
