class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        numSum = sum(nums[:k])
        maxSum = numSum
        i = k
        while i < n:
            numSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, numSum)
            i += 1
        return maxSum / float(k)
