from typing import List
from heapq import heappush, heappop


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i, num in enumerate(nums):
            heappush(pq, (num, i))

        while k > 0:
            value, idx = heappop(pq)
            value *= multiplier
            heappush(pq, (value, idx))
            k -= 1

        while pq:
            value, idx = heappop(pq)
            nums[idx] = value

        return nums
