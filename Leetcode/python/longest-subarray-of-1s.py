class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        zeros = 0
        res = 0

        for r in range(n):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r - l + 1 - zeros)
        return res - 1 if res == n else res
