class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        freq = {}
        l = 0
        n = len(nums)

        for r in range(n):
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            if freq[nums[r]] > k:
                while nums[l] != nums[r]:
                    freq[nums[l]] -= 1
                    l += 1

                freq[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
