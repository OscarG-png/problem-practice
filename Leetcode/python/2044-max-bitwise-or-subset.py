from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0

        for n in nums:
            maxOr |= n

        res = 0
        def dfs(i, currOr):
            nonlocal res, maxOr
            if i == len(nums):
                res += 1 if currOr == maxOr else 0
                return
            dfs(i + 1, currOr)
            dfs(i + 1, currOr | nums[i])
        dfs(0, 0)
        return res
