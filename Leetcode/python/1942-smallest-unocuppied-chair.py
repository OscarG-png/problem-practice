from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        indexes = [i for i in range(len(times))]
        indexes.sort(key=lambda i: times[i][0])

        usedChairs = []
        availableChairs = [i for i in range(len(times))]

        for i in indexes:
            a, l = times[i]
            while usedChairs and usedChairs[0][0] <= a:
                leave, chair = heapq.heappop(usedChairs)
                heapq.heappush(availableChairs, chair)
            chair = heapq.heappop(availableChairs)
            heapq.heappush(usedChairs, (l, chair))

            if i == targetFriend:
                return chair
        return -1
