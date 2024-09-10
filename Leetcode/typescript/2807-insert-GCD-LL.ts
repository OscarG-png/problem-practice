// Definition for singly-linked list.
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function insertGreatestCommonDivisors(head: ListNode | null): ListNode | null {
  function gcd(a: number, b: number) {
    if (!b) return a;
    return gcd(b, a % b);
  }
  if (!head) return null;
  let curr = head;
  while (curr.next) {
    const [n1, n2] = [curr.val, curr.next.val];
    curr.next = new ListNode(gcd(n1, n2), curr.next);
    curr = curr.next.next;
  }
  return head;
}
