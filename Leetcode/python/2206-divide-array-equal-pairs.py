from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        oddSet = set()

        for num in nums:
            if num not in oddSet:
                oddSet.add(num)
            else:
                oddSet.remove(num)

        return len(oddSet) == 0
