# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        children = set()

        for par, child, is_left in descriptions:
            children.add(child)
            if par not in nodeMap:
                nodeMap[par] = TreeNode(par)
            if child not in nodeMap:
                nodeMap[child] = TreeNode(child)

            if is_left:
                nodeMap[par].left = nodeMap[child]
            else:
                nodeMap[par].right = nodeMap[child]

        for p, c, l in descriptions:
            if p not in children:
                return nodeMap[p]
