# https://leetcode.com/explore/interview/card/google/59/array-and-strings/339/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plusOne = [int(elem) for elem in str(int(''.join([str(elem) for elem in digits])) + 1)]
        return [0] * (len(digits) - len(plusOne)) + plusOne


print(Solution().plusOne([1, 2, 3]))  # [1,2,4]
print(Solution().plusOne([4, 3, 2, 1]))  # [4,3,2,2]
print(Solution().plusOne([0]))  # [1]
print(Solution().plusOne([9]))  # [1, 0]
print(Solution().plusOne([0, 0]))  # [0, 1]
print(Solution().plusOne([9, 9]))  # [1, 0, 0]

