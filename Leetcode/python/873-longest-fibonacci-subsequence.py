from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arrSet = set(arr)
        res = 0

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev, curr = arr[i], arr[j]
                nxtNum = prev + curr
                length = 2
                while nxtNum in arrSet:
                    length += 1
                    prev, curr = curr, nxtNum
                    nxtNum = prev + curr
                    res = max(res, length)

        return res
