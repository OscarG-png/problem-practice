function containsDuplicate(nums: number[]): boolean {
  let count: Set<number> = new Set();

  for (let num of nums) {
    if (count.has(num)) {
      return true;
    } else {
      count.add(num);
    }
  }
  return false;
}
