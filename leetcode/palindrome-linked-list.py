# https://leetcode.com/problems/palindrome-linked-list/
# 파이썬 알고리즘 인터뷰 책 참고 p.201

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev


print(Solution().isPalindrome(ListNode(1, ListNode(2))))  # false
print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))  # true
