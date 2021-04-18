# https://leetcode.com/problems/median-of-two-sorted-arrays/
import heapq
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = list(heapq.merge(nums1, nums2))
        if (len(nums1) + len(nums2)) % 2 == 0:
            return sum(l[int((len(nums1) + len(nums2)) / 2) - 1:int((len(nums1) + len(nums2)) / 2) + 1]) / 2
        else:
            return l[int((len(nums1) + len(nums2)) / 2)]


print(Solution().findMedianSortedArrays(nums1=[], nums2=[1, 2, 3, 4, 5]))  # 3
print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))  # 2.5
print(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]))  # 2
print(Solution().findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]))  # 0
print(Solution().findMedianSortedArrays(nums1=[], nums2=[1]))  # 1
print(Solution().findMedianSortedArrays(nums1=[2], nums2=[]))  # 2
