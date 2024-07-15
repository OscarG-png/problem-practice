class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxCount = 0
        maxIndex = 0

        for i, row in enumerate(mat):
            currCount = row.count(1)
            if currCount > maxCount:
                maxCount = currCount
                maxIndex = i
        return [maxIndex, maxCount]
