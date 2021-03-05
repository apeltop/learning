# https://leetcode.com/problems/daily-temperatures/
# 파이썬 알고리즘 인터뷰 책 참고 p.252
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


print(Solution().dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
