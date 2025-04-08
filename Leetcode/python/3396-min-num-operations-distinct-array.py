from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)

        def isDistinct():
            return all(v <= 1 for v in freq.values())

        if isDistinct():
            return 0

        res = 0
        while nums:
            if len(nums) < 3:
                return res + 1
            for i in range(3):
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            nums = nums[3:]
            res += 1
            if isDistinct():
                return res
        return res
