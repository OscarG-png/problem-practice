from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total = 0
        for row in grid:
            for n in row:
                total += n
                if n % x != grid[0][0] % x:
                    return -1

        nums = [n for row in grid for n in row]
        nums.sort()

        prefix = 0
        res = float('inf')

        for i in range(len(nums)):
            costLeft = nums[i] * i - prefix
            costRight = total - prefix - (nums[i] * (len(nums) - i))
            operations = (costLeft + costRight) // x
            res = min(res, operations)

            prefix += nums[i]
        return res
