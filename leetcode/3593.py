# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head or head.next is None:
#             return head
#
#         prev = None
#         cur = head
#         uniqueNode = None
#
#         while cur:
#             if cur == head:
#                 if cur.val != cur.next.val:
#                     uniqueNode = ListNode(cur.val)
#             elif cur.next is None:
#                 if cur.val != prev.val:
#                     if not uniqueNode:
#                         uniqueNode = ListNode(cur.val)
#                     else:
#                         c = uniqueNode
#                         while c.next:
#                             c = c.next
#                         c.next = ListNode(cur.val)
#             elif cur.val != prev.val and cur.val != cur.next.val:
#                 if not uniqueNode:
#                     uniqueNode = ListNode(cur.val)
#                 else:
#                     c = uniqueNode
#                     while c.next:
#                         c = c.next
#                     c.next = ListNode(cur.val)
#
#             prev = cur
#             cur = cur.next
#
#         return uniqueNode

def skipDups(head: ListNode):
    if not head or not head.next:
        # List only has a single elemnet
        return head

    if head.val == head.next.val:
        # Remove the duplicated element
        r = skipDups(head.next)
        return r.next if r == head.next else r

    head.next = skipDups(head.next)

    return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return skipDups(head)

c = ListNode(1, ListNode(1))
print(Solution().deleteDuplicates(head=c))

a = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(5)))))
print(Solution().deleteDuplicates(head=a))
print()

d = ListNode(1, ListNode(1, ListNode(2)))
print(Solution().deleteDuplicates(head=d))
print()

b = ListNode(1)
print(Solution().deleteDuplicates(head=b))
print()


e = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
print(Solution().deleteDuplicates(head=e))
print()

f = ListNode(1, ListNode(2))
print(Solution().deleteDuplicates(head=f))
