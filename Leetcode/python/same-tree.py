# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue_p = [p]
        queue_q = [q]

        while queue_p and queue_q:
            p_node = queue_p.pop(0)
            q_node = queue_q.pop(0)

            if (not p_node and q_node) or (p_node and not q_node):
                return False
            if p_node and q_node and p_node.val != q_node.val:
                return False
            if p_node:
                queue_p.append(p_node.left)
                queue_p.append(p_node.right)
            if q_node:
                queue_q.append(q_node.left)
                queue_q.append(q_node.right)
        return True
