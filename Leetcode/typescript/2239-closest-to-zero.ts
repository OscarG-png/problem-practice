function findClosestNumber(nums: number[]): number {
  let closest = nums[0];

  for (const num of nums) {
    if (Math.abs(num) < Math.abs(closest)) {
      closest = num;
    }
  }
  if (cloest < 0 && nums.includes(Math.abs(closest))) {
    return Math.abs(closest);
  }
  return closest;
}
