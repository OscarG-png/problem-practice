# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        stack = [root]
        while stack:
            current = stack.pop()

            current.left, current.right = current.right, current.left

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return root
