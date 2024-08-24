function canJump(nums: number[]): boolean {
  let current = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (current === 0) return false;
    current--;
    current = Math.max(current, nums[i]);
  }
  return true;
}
