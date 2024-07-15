# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        hashMap = {
            "odd": 0,
            "even": 0
        }

        while head and head.next:
            even = head.val
            odd = head.next.val

            if even > odd:
                hashMap["even"] += 1
            else:
                hashMap["odd"] += 1
            head = head.next.next
        if hashMap["odd"] > hashMap["even"]:
            return "Odd"
        elif hashMap["even"] > hashMap["odd"]:
            return "Even"
        else:
            return "Tie"
