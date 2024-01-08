class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for num in nums:
            result[num] = result.get(num, 0) + 1
        return max(result, key=result.get)
