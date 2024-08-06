function minimumPushes(word: string): number {
  let counts = new Array(26).fill(0);

  for (const c of word) {
    counts[c.charCodeAt(0) - "a".charCodeAt(0)]++;
  }
  counts.sort();
  let res = 0;
  let distinct = 0;

  for (const cnt of counts) {
    res += cnt * (1 + Math.floor(distinct / 8));
    distinct++;
  }
  return res;
}
