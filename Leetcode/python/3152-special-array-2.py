from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            if (nums[i - 1] % 2 == 0 and nums[i] % 2== 0) or (nums[i - 1] % 2 != 0 and nums[i] % 2 != 0):
                prefix[i] += 1

        result = []

        for start, stop in queries:
            count = prefix[stop] - (prefix[start] if start > 0 else 0)
            result.append(count == 0)
        return result
