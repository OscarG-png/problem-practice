from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subArrSums = []
        MOD = 10 ** 9 + 7

        for i in range(n):
            currSum = 0
            for j in range(i, n):
                currSum = (currSum + nums[j]) % MOD
                subArrSums.append(currSum)

        subArrSums.sort()
        res = 0
        for i in range(left - 1, right):
            res = (res + subArrSums[i]) % MOD

        return res
