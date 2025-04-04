from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return (None, 0)

            leftNode, leftHeight = dfs(node.left)
            rightNode, rightHeight = dfs(node.right)

            if leftHeight > rightHeight:
                return leftNode, leftHeight + 1
            elif leftHeight < rightHeight:
                return rightNode, rightHeight + 1
            return node, 1 + leftHeight

        node, _ = dfs(root)
        return node
