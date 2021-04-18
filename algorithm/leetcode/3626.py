# https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


root1 = TreeNode(1, TreeNode(0), TreeNode(2))
print(Solution().trimBST(root1, 1, 2))  # [1, null, 2]

root2 = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))
print(Solution().trimBST(root2, 1, 3))  # [3, 2, null, 1]

root3 = TreeNode(1)
print(Solution().trimBST(root3, 1, 2))  # [1]

root4 = TreeNode(1, None, TreeNode(2))
print(Solution().trimBST(root4, 1, 3))  # [1, null, 3]

root5 = TreeNode(1, None, TreeNode(2))
print(Solution().trimBST(root5, 2, 4))  # [2]
