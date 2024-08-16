from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        currMin, currMax = arrays[0][0], arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(
                res,
                arr[-1] - currMin,
                currMax - arr[0]
            )
            currMin = min(currMin, arr[0])
            currMax = max(currMax, arr[-1])

        return res
