function maxKelements(nums: number[], k: number): number {
  let res = 0;

  const maxHeap = new MaxPriorityQueue({ priority: (x) => x });

  for (const n of nums) {
    maxHeap.enqueue(n);
  }
  while (k > 0) {
    const n = maxHeap.dequeue().element;
    res += n;
    k--;
    maxHeap.enqueue(Math.ceil(n / 3));
  }

  return res;
}
