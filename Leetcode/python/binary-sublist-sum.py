class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        currSum = 0
        totalSubarrays = 0

        for num in nums:
            currSum += num
            if currSum - goal in count:
                totalSubarrays += count[currSum - goal]
            count[currSum] = count.get(currSum, 0) + 1

        return totalSubarrays
