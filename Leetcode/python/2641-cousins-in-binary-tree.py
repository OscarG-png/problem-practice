from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        levelSum = []

        q = deque([root])
        while q:
            currSum = 0
            for i in range(len(q)):
                node = q.popleft()
                currSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelSum.append(currSum)

        q = deque([(root, root.val)])
        level = 0
        while q:
            for i in range(len(q)):
                node, val = q.popleft()
                node.val = levelSum[level] - val

                childSum = 0
                if node.left:
                    childSum += node.left.val
                if node.right:
                    childSum += node.right.val

                if node.left:
                    q.append((node.left, childSum))
                if node.right:
                    q.append((node.right, childSum))
            level += 1
        return root
