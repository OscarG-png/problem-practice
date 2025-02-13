import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0

        while len(nums) > 1:
            smallest = heapq.heappop(nums)
            if smallest >= k:
                return operations
            secondSmallest = heapq.heappop(nums)
            newElement = min(smallest, secondSmallest) * 2 + max(smallest, secondSmallest)
            heapq.heappush(nums, newElement)
            operations += 1

        return operations if nums[0] >= k else -1
