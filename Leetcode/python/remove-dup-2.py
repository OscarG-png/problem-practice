class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        count = 1

        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]:
                count += 1
                if count <= 2:
                    slow += 1
                    nums[slow] = nums[fast]
            else:
                count = 1
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
