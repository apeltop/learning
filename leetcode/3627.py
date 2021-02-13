# https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3627/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head and head.next is not None:
            if head.val == 'PASS':
                return True
            head.val = 'PASS'
            head = head.next

        return False


list1 = ListNode(3)
list1_1 = ListNode(2)
list1_2 = ListNode(0)
list1_3 = ListNode(-4)
list1.next = list1_1
list1_1.next = list1_2
list1_2.next = list1_3
list1_3.next = list1_1
print(Solution().hasCycle(list1))  # true

list2 = ListNode(1)
list2_1 = ListNode(2)
list2.next = list2_1
list2_1.next = list2
print(Solution().hasCycle(list2))  # true

list3 = ListNode(3)
print(Solution().hasCycle(list3))  # false
