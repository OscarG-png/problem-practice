// def for list node
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function deleteDuplicates(head: ListNode | null): ListNode | null {
  let curr = head;

  while (curr) {
    while (curr.next && curr.next.val === curr.val) {
      curr.next = curr.next.next;
    }
    curr = curr.next;
  }
  return head;
}
