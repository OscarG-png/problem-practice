from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        currSum = 0
        l = 0
        for r in range(len(nums)):
            currSum += nums[r]
            count[nums[r]] += 1

            if r - l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                currSum -= nums[l]
                l += 1

            if len(count) == r - l + 1 == k:
                res = max(res, currSum)
        return res
