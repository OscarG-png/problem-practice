class MyCalendarTwo:

    def __init__(self):
        self.nonOverlapping = []
        self.overlapping = []


    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not (end <= s or e <= start):
                return False
        for s, e in self.nonOverlapping:
            if end > s and e > start:
                self.overlapping.append(
                    (max(s, start), min(e, end))
                )
        self.nonOverlapping.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
