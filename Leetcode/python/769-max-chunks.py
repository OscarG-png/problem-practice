from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        currMax = -1
        res = 0

        for i, n in enumerate(arr):
            currMax = max(n, currMax)

            if currMax == i:
                res += 1
        return res
