# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        hashMap = {}
        queue = [[0, root]]

        while queue:
            depth, curr = queue.pop(0)
            if depth not in hashMap:
                hashMap[depth] = []
            hashMap[depth].append(curr.val)

            if curr.left:
                queue.append([depth + 1, curr.left])
            if curr.right:
                queue.append([depth + 1, curr.right])

        res = [
            value for value in hashMap.values()
        ]
        return res
