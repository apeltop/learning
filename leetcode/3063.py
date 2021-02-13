# https://leetcode.com/explore/featured/card/google/60/linked-list-5/3063/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1List, l2List = [], []

        while l1 is not None:
            l1List.append(str(l1.val))
            l1 = l1.next

        while l2 is not None:
            l2List.append(str(l2.val))
            l2 = l2.next

        l1List.reverse()
        l2List.reverse()

        result = str(int(''.join(l1List)) + int(''.join(l2List)))[::-1]

        resultHead = ListNode(int(result[0]))
        resultNode = resultHead
        for c in result[1:]:
            newNode = ListNode(int(c))
            resultNode.next = newNode
            resultNode = resultNode.next

        return resultHead


print(
    Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))  # [7, 0, 8]
print(Solution().addTwoNumbers(ListNode(0), ListNode(0)))  # [0]
print(Solution().addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))  # [8,9,9,9,0,0,0,1]
