class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([
            item[0] for item in intervals
        ])
        end = sorted([
            item[1] for item in intervals
        ])
        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
