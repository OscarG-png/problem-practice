from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n

        dp = [0] * (size + 1)

        for row in grid:
            for num in row:
                dp[num] += 1

        repeated = -1
        missing = -1

        for num in range(1, size + 1):
            if dp[num] == 2:
                repeated = num
            if dp[num] == 0:
                missing = num

        return [repeated, missing]
