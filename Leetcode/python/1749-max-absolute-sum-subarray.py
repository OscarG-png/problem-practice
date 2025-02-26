from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minPre, maxPre = 0, 0
        currSum = 0
        res = 0

        for n in nums:
            currSum += n
            res = max(res, abs(currSum - minPre), abs(currSum - maxPre))
            minPre = min(minPre, currSum)
            maxPre = max(maxPre, currSum)

        return res
