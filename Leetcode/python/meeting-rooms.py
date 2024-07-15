class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True

# changing sort from just intervals.sort() to intervals.sort(key = lambda x: x[0]) decreased my runtime from 83 to 72 ms
