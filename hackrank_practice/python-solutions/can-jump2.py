class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        current = nums[0]
        jumps = 1
        steps = nums[0]

        for i in range(1, len(nums)):
            if i == len(nums) - 1:
                return jumps

            current = max(current, i + nums[i])
            steps -= 1

            if steps == 0:
                jumps += 1
                steps = current - i

# not great on runtime or memory usage but we got there
