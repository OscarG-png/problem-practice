function minGroups(intervals: number[][]): number {
  let start: number[] = [];
  let end: number[] = [];

  for (const [l, r] of intervals) {
    start.push(l);
    end.push(r);
  }
  start.sort((a, b) => a - b);
  end.sort((a, b) => a - b);

  let i = 0;
  let j = 0;
  let res = 0;

  while (i < intervals.length && j < intervals.length) {
    if (start[i] <= end[j]) {
      i++;
    } else {
      j++;
    }
    res = Math.max(res, i - j);
  }

  return res;
}
