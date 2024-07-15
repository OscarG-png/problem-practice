class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if self.product(nums) > 0:
            return 1
        elif self.product(nums) < 0:
            return -1
        else:
            return 0

    def product(self, nums):
        total = 1

        for num in nums:
            total *= num
        return total
