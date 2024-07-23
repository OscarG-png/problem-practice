from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        res = sorted(nums, key=lambda x: (freqMap[x], -x))
        return res
