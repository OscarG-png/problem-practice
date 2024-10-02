from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(list(set(arr)))
        numMap = {}

        for i in range(len(sortedArr)):
            numMap[sortedArr[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = numMap[arr[i]]

        return arr
