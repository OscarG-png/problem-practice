from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        count = Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res
