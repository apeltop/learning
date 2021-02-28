# https://leetcode.com/problems/swap-nodes-in-pairs/
# 파이썬 알고리즘 인터뷰 책 참고 p.231

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head


print(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))  # [2, 1, 4, 3]
print(Solution().swapPairs(ListNode(1)))  # [1]
print(Solution().swapPairs(None))  # []
