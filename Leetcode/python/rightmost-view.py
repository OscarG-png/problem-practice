# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        if not root:
            return res

        while stack:
            rightMost = None
            n = len(stack)

            for i in range(n):
                curr = stack.pop(0)
                if curr:
                    rightMost = curr
                    stack.append(curr.left)
                    stack.append(curr.right)
            if rightMost:
                res.append(rightMost.val)
        return res
