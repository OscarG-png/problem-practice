from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThan = []
        pivotList = []
        moreThan = []

        for num in nums:
            if num < pivot:
                lessThan.append(num)
            elif num == pivot:
                pivotList.append(num)
            else:
                moreThan.append(num)

        return lessThan + pivotList + moreThan
