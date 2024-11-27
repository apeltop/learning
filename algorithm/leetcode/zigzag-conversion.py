# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        y, x = 0, 0
        maps = ['' for _ in range(len(s) * numRows)]

        is_decent = True
        for a in s:
            maps[y * len(s) + x] = a

            if y == 0:
                is_decent = True

            if y == numRows - 1:
                is_decent = False

            if is_decent:
                y += 1
            else:
                y -= 1
                x += 1
            y = max(y, 0)

        return ''.join([a for a in maps if a != ''])

print(Solution().convert( s = "AAAAAA", numRows = 1), "AAAAAA")
print(Solution().convert( s = "PAYPALISHIRING", numRows = 3), "PAHNAPLSIIGYIR")
print(Solution().convert( s = "PAYPALISHIRING", numRows = 4), "PINALSIGYAHRPI")
print(Solution().convert( s = "A", numRows = 1), "A")
