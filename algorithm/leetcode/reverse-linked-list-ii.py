# https://leetcode.com/problems/reverse-linked-list-ii/
# 파이썬 알고리즘 인터뷰 책 참고 p.237

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next


print(Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4))  # [1,4,3,2,5]
print(Solution().reverseBetween(ListNode(5), 1, 1))  # [5]
