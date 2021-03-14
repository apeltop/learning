# https://leetcode.com/problems/merge-k-sorted-lists/
# 파이썬 알고리즘 인터뷰 책 참고 p.274

# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


print(Solution().mergeKLists(lists=[ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))),
                                    ListNode(2, ListNode(6))]))  # [1,1,2,3,4,4,5,6]
