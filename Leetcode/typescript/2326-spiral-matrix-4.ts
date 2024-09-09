// Definition for singly-linked list.
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function spiralMatrix(m: number, n: number, head: ListNode | null): number[][] {
  const res: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
  let top = 0,
    bottom = m - 1,
    left = 0,
    right = n - 1;

  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let [r, c, d] = [0, 0, 0]; //row, coloumn, direction

  while (head) {
    res[r][c] = head.val;
    head = head.next;
    const [dr, dc] = directions[d];
    const [nr, nc] = [r + dr, c + dc];
    if (
      nr < top ||
      nr > bottom ||
      nc < left ||
      nc > right ||
      res[nr][nc] !== -1
    ) {
      d = (d + 1) % 4;
      r += directions[d][0];
      c += directions[d][1];
    } else {
      r = nr;
      c = nc;
    }
  }
  return res;
}
