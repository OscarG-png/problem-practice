from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        res = len(nums)
        currSum = 0
        remainderIndex = {
            0: -1
        }

        for i, n in enumerate(nums):
            currSum = (currSum + n) % p
            prefix = (currSum - remain + p) % p
            if prefix in remainderIndex:
                length = i - remainderIndex[prefix]
                res = min(res, length)
            remainderIndex[currSum] = i

        return -1 if res == len(nums) else res
