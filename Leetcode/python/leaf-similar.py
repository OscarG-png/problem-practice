# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return self.dfs(node.left) + self.dfs(node.right)


# had to make a function to see if the leaves from two different
# trees are the same. I did this by using a dfs function to compare the leaves
# values
