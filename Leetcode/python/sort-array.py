from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            leftMerge = mergeSort(arr[:mid])
            rightMerge = mergeSort(arr[mid:])
            return merge(leftMerge, rightMerge)

        def merge(left, right):
            sortedList = []
            leftIndex, rightIndex = 0, 0

            while leftIndex < len(left) and rightIndex < len(right):
                if left[leftIndex] < right[rightIndex]:
                    sortedList.append(left[leftIndex])
                    leftIndex += 1
                else:
                    sortedList.append(right[rightIndex])
                    rightIndex += 1

            while leftIndex < len(left):
                sortedList.append(left[leftIndex])
                leftIndex += 1
            while rightIndex < len(right):
                sortedList.append(right[rightIndex])
                rightIndex += 1
            return sortedList

        return mergeSort(nums)
