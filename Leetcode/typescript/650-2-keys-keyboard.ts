function minSteps(n: number): number {
  let cache = new Map();

  function helper(count: number, paste: number) {
    if (count === n) {
      return 0;
    }
    if (count > n) {
      return 1000;
    }
    const key = `${count}, ${paste}`;
    if (cache.has(key)) {
      return cache.get(key);
    }
    const res1 = 1 + helper(count + paste, paste);
    const res2 = 2 + helper(count + count, count);
    const res = Math.min(res1, res2);
    cache.set(key, res);
    return res;
  }
  if (n === 1) {
    return 0;
  }
  return 1 + helper(1, 1);
}
