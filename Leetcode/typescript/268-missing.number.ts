function missingNumber(nums: number[]): number {
  const n = nums.length;

  let check = new Array(n + 1).fill(-1);

  for (const num of nums) {
    check[num] = num;
  }

  for (let i = 0; i < check.length; i++) {
    if (check[i] === -1) {
      return i;
    }
  }
  return 0;
}
