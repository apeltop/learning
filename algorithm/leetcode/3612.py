# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3612/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) - len(t) > 1 or s == t:
            return False

        s = list(s)
        t = list(t)

        apart = []

        while s and t:
            lElemS = s.pop()
            lElemT = t.pop()

            if lElemS != lElemT:
                if apart:
                    return False

                if len(s) < len(t):
                    apart.append(lElemT)
                    s.append(lElemS)
                elif len(s) > len(t):
                    apart.append(lElemS)
                    t.append(lElemT)
                else:
                    apart.append(lElemS)

        return False if apart and (s or t) else True


# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         n, m = len(s), len(t)
#         i = 0
#         while i < n and i < m:
#             if s[i] != t[i]:
#                 if s[i + 1:] == t[i + 1:] or s[i + 1:] == t[i:] or s[i:] == t[i + 1:]:
#                     return True
#                 return False
#             i += 1
#
#         return abs(m - n) == 1


print(Solution().isOneEditDistance("ac", "a"))  # true
print(Solution().isOneEditDistance("abcd", "bbd"))  # false
print(Solution().isOneEditDistance("a", ""))  # true
print(Solution().isOneEditDistance("", "A"))  # true
print(Solution().isOneEditDistance("ab", "acb"))  # true
print(Solution().isOneEditDistance("", ""))  # false
