from typing import List
from collections import defaultdict


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        targetMap = defaultdict(int)

        for n1, n2 in zip(target, arr):
            targetMap[n1] += 1
            targetMap[n2] -= 1

        for n in targetMap:
            if targetMap[n] != 0:
                return False

        return True
