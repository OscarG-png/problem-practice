from typing import List
from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        numToGroup = {}

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())

            groups[-1].append(n)
            numToGroup[n] = len(groups) - 1

        res = []
        for n in nums:
            j = numToGroup[n]
            res.append(groups[j].popleft())

        return res
