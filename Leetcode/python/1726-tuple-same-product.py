from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        productCount = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                productCount[product] += 1

        res = 0
        for cnt in productCount.values():
            pairs = (cnt * (cnt - 1)) // 2
            res += 8 * pairs
        return res
