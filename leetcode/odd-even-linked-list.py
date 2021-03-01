# https://leetcode.com/problems/odd-even-linked-list/
# 파이썬 알고리즘 인터뷰 책 참고 p.233

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head


print(Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))  # 1->3->5->2->4->NULL
print(Solution().oddEvenList(ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(
    7)))))))))  # 2->3->6->7->1->5->4->NULL
