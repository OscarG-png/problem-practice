function numJewelsInStones(jewels: string, stones: string): number {
  let jewelMap = new Set([...jewels]);
  let res = 0;
  for (const c of stones) {
    if (jewelMap.has(c)) {
      res += 1;
    }
  }
  return res;
}
