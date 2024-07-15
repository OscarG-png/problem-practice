class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sumNum, result, j = 0, 0, 0

        for i, n in enumerate(nums):
            sumNum += n
            while sumNum * (i - j + 1) >= k:
                sumNum -= nums[j]
                j += 1
            result += i - j + 1
        return result
