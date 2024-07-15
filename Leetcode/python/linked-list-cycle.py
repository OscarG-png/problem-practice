# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        seen = set()
        queue = [head]

        while queue:
            current = queue.pop(0)

            if current.next:
                if current.next in seen:
                    return True
                queue.append(current.next)
            seen.add(current)
        return False
