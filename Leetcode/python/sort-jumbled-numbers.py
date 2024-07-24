from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i, n in enumerate(nums):
            n = str(n)
            mappedN = 0

            for c in n:
                mappedN *= 10
                mappedN += mapping[int(c)]
            pairs.append((mappedN, i))

        pairs.sort()

        return [nums[p[1]] for p in pairs]
