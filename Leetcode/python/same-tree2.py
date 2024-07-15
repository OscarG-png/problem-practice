# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackP = [p]
        stackQ = [q]

        while stackP and stackQ:
            currP = stackP.pop()
            currQ = stackQ.pop()
            if (not currP and currQ) or (currP and not currQ):
                return False
            if currP and currQ and currP.val != currQ.val:
                return False
            if currP:
                stackP.append(currP.left)
                stackP.append(currP.right)
            if currQ:
                stackQ.append(currQ.left)
                stackQ.append(currQ.right)
        return True

# This version with a DFS search was significantly faster than the BFS version.
