# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isEven(val):
            return val % 2 == 0

        queue = [[root, 0]]

        while queue:
            prevVal = None
            depthLen = len(queue)

            for _ in range(depthLen):
                curr, depth = queue.pop(0)

                if depth % 2 == 0:
                    if isEven(curr.val) or (prevVal is not None and curr.val <= prevVal):
                        return False
                else:
                    if not isEven(curr.val) or (prevVal is not None and curr.val >= prevVal):
                        return False
                prevVal = curr.val

                if curr.left:
                    queue.append([curr.left, depth + 1])
                if curr.right:
                    queue.append([curr.right, depth + 1])
        return True
