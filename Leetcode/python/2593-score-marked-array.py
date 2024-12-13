from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        sortedNums = sorted((num, idx) for idx, num in enumerate(nums))
        score = 0

        for num, idx in sortedNums:
            if nums[idx] != -1:
                score += num
                nums[idx] = -1
                if idx > 0:
                    nums[idx - 1] = -1
                if idx < n - 1:
                    nums[idx + 1] = -1

        return score
