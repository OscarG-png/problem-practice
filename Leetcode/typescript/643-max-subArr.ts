function findMaxAverage(nums: number[], k: number): number {
  const n = nums.length;
  let numSum = nums.slice(0, k).reduce((a, b) => a + b, 0);
  let maxSum = numSum;

  for (let i = k; i < n; i++) {
    numSum += nums[i] - nums[i - k];
    maxSum = Math.max(maxSum, numSum);
  }
  return maxSum / k;
}
