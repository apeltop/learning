from typing import List


# 파이썬 알고리즘 인터뷰 책 참고 p.146
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # if s type == string
        # s[:] = s[::-1]
        s.reverse()


print(Solution().reverseString(["h", "e", "l", "l", "o"]))  # ["o","l","l","e","h"]
print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))  # ["h","a","n","n","a","H"]
