# https://leetcode.com/problems/reverse-linked-list/
# 파이썬 알고리즘 인터뷰 책 참고 p.219

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverseHead = None

        while head is not None:
            newNode = ListNode(head.val)
            newNode.next = reverseHead
            reverseHead = newNode

            head = head.next

        return reverseHead

        # 파이썬 알고리즘 인터뷰 책 풀이 1. 재귀 구조로 뒤집기
        # def reverse(node: ListNode, prev: ListNode = None):
        #     if not node:
        #         return prev
        #
        #     next, node.next = node.next, prev
        #     return reverse(next, node)
        #
        # return reverse(head)

        # 파이썬 알고리즘 인터뷰 책 풀이 2. 반복 구조로 뒤집기
        # node, prev = head, None
        #
        # while node:
        #     next, node.next = node.next, prev
        #     prev, node = node, next
        #
        # return prev


print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))  # [5, 4, 3, 2, 1]
print(Solution().reverseList(ListNode(1, ListNode(2))))  # [2, 1]
print(Solution().reverseList(ListNode(None)))  # []
