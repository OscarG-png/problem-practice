from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        oddNode = curr = head
        evenNode = evenStart = head.next
        i = 1

        while curr:
            if i > 2 and i % 2 != 0:
                oddNode.next = curr
                oddNode = oddNode.next
            elif i > 2 and i % 2 == 0:
                evenNode.next = curr
                evenNode = evenNode.next
            curr = curr.next
            i += 1
        evenNode.next = None
        oddNode.next = evenStart
        return head
