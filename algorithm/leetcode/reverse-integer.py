# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        v = str(x)[::-1]

        is_posi = True
        if v[-1] == '-':
            is_posi = False
            v = v[:-1]
        v = int(v)
        v = v if is_posi else v * -1
        if -(2 ** 31) <= v <= (2 ** 31) - 1:
            return v
        return 0
        # print(2 ** 32)
# -2 31 <= x <= 2 31 - 1

print(Solution().reverse(2 ** 10), 0)
print(Solution().reverse(123), 321)
print(Solution().reverse(-123), -321)
print(Solution().reverse(120), 21)
print(Solution().reverse(2 ** 30), 0)
print(Solution().reverse(2 ** 31), 0)
