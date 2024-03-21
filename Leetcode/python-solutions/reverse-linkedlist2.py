# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next = current.next
            prev, current.next = current, prev
            current = next
        return prev

# almost same as my previous solution. This one uses less memory since i'm not assinging head to curr.
