from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []

        for start, end in intervals:
            start.append(start)
            end.append(end)

        start.sort()
        end.sort()

        i, j = 0, 0
        res = 0

        while i < len(intervals) and j < len(intervals):
            if start[i] <= end[j]:
                i += 1
            else:
                j += 1
            res = max(res, i - j)
        return res
