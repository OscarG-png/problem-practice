# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        stack = [root]
        total = 0

        while stack:
            current = stack.pop()
            if current:
                if low <= current.val <= high:
                    total += current.val
                if current.val > low:
                    stack.append(current.left)
                if current.val < high:
                    stack.append(current.right)
        return total
