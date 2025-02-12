from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        maxArr = [0] * 82

        def sumDigits(n: int) -> int:
            return sum(int(digit) for digit in str(n))

        for num in nums:
            digitSum = sumDigits(num)
            if maxArr[digitSum] != 0:
                res = max(res, num + maxArr[digitSum])
            maxArr[digitSum] = max(maxArr[digitSum], num)

        return res
