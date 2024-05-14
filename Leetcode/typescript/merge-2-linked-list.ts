/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  if (!list1) return list2;
  if (!list2) return list1;

  let merged: ListNode = new ListNode();
  let head: ListNode = merged;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      merged.next = list1;
      list1 = list1.next;
    } else {
      merged.next = list2;
      list2 = list2.next;
    }
    merged = merged.next;
  }
  if (list1) {
    merged.next = list1;
  } else {
    merged.next = list2;
  }
  return head.next;
}
