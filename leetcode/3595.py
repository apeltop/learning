# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_substring = deque()
        cur_substring = deque()
        for a in s:
            if a in cur_substring:
                while cur_substring and cur_substring[0] != a:
                    cur_substring.popleft()
                cur_substring.popleft()

            cur_substring.append(a)
            if len(long_substring) < len(cur_substring):
                long_substring = cur_substring.copy()

        return len(long_substring)


print(Solution().lengthOfLongestSubstring('abcabcbb'))  # 3
print(Solution().lengthOfLongestSubstring('bbbb'))  # 1
print(Solution().lengthOfLongestSubstring('pwwkew'))  # 3
