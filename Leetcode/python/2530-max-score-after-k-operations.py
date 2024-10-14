from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
            res = 0
            maxHeap = [-n for n in nums]
            heapq.heapify(maxHeap)

            while k:
                n = -heapq.heappop(maxHeap)
                res += n
                k -= 1
                heapq.heappush(maxHeap, -math.ceil(n / 3))

            return res
