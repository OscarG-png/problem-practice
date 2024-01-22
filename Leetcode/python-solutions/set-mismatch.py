class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dupe = 0
        missing = 0

        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                dupe = i
            elif count == 0:
                missing = i
        return [dupe, missing]
