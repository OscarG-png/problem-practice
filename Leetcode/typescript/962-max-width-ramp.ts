function maxWidthRamp(nums: number[]): number {
  let maxRight = new Array(nums.length).fill(0);
  let i = nums.length - 1;
  let prevMax = 0;

  for (let j = nums.length - 1; j >= 0; j--) {
    maxRight[i] = Math.max(nums[j], prevMax);
    prevMax = maxRight[i];
    i--;
  }

  let res = 0;
  let l = 0;

  for (let r = 0; r < nums.length; r++) {
    while (nums[l] > maxRight[r]) {
      l++;
    }
    res = Math.max(res, r - l);
  }
  return res;
}
