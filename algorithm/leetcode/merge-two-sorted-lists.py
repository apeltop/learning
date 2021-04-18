# https://leetcode.com/problems/merge-two-sorted-lists/
# 파이썬 알고리즘 인터뷰 책 참고 p.213


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1


print(Solution().mergeTwoLists(l1=ListNode(1, ListNode(2, ListNode(4))),
                               l2=ListNode(1, ListNode(3, ListNode(4)))))  # [1,1,2,3,4,4]
print(Solution().mergeTwoLists(l1=ListNode(), l2=ListNode()))  # []
print(Solution().mergeTwoLists(l1=ListNode(), l2=ListNode(0)))  # [0]
