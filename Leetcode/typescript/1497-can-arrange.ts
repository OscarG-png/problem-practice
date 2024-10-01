function canArrange(arr: number[], k: number): boolean {
  const remainderCount: Map<number, number> = new Map();

  for (let num of arr) {
    let remainder = num % k;
    if (remainder < 0) {
      remainder += k;
    }
    remainderCount.set(remainder, (remainderCount.get(remainder) || 0) + 1);
  }

  for (let [rem, count] of remainderCount) {
    if (rem === 0) {
      if (count % 2 !== 0) return false;
    } else if (rem * 2 === k) {
      if (count % 2 !== 0) return false;
    } else {
      const complementCount = remainderCount.get(k - rem) || 0;
      if (count !== complementCount) return false;
    }
  }
  return true;
}
