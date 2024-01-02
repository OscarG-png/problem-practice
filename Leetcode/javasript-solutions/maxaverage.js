var findMaxAverage = function(nums, k) {
    let n = nums.length;
    let numSum = 0;

    for (let i = 0; i < k; i++) {
        numSum += nums[i];
    }

    let maxSum = numSum;
    for (let i = k; i < n; i++) {
        numSum += nums[i] - nums[i - k];
        maxSum = Math.max(maxSum, numSum);
    }
    return maxSum / k;
};
