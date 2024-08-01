# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, routeMax):
            if not node:
                return 0
            currMax = max(routeMax, node.val)
            val = dfs(node.left, currMax) + dfs(node.right, currMax)
            if node.val >= currMax:
                val += 1
            return val

        return dfs(root, root.val)
