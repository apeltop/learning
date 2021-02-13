# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        return haystack.find(needle)


print(Solution().strStr(haystack="hello", needle="ll"))  # 2
print(Solution().strStr(haystack="aaaaa", needle="bba"))  # -1
print(Solution().strStr(haystack="", needle=""))  # 0
