class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current = nums[0]

        for i in range(1, len(nums)):
            if current == 0:
                return False
            current -= 1
            current = max(current, nums[i])
        return True

# run time is pretty slow but memory usage is good
