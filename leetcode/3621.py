# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3621/

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = collections.deque([(root, 0, 0)])
        depth = 0

        traversalDict = collections.defaultdict(list)

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root, row, col = queue.popleft()
                traversalDict[col].append((cur_root.val, row, col))
                if cur_root.left:
                    queue.append((cur_root.left, row + 1, col - 1))
                if cur_root.right:
                    queue.append((cur_root.right, row + 1, col + 1))

        traversalList = []
        for k in sorted(traversalDict.keys()):
            traversalList.append([elem[0] for elem in sorted(traversalDict[k], key=lambda x: (x[1], x[0]))])

        return traversalList


root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
root3 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(5), TreeNode(7)))
root4 = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(4, TreeNode(2)))

print(Solution().verticalTraversal(root=root1))  # [[9],[3,15],[20],[7]]
print(Solution().verticalTraversal(root=root2))  # [[4],[2],[1,5,6],[3],[7]]
print(Solution().verticalTraversal(root=root3))  # [[4],[2],[1,5,6],[3],[7]]
print(Solution().verticalTraversal(root=root4))  # [[0],[1],[3,2,2],[4]]
