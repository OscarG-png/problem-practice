from collections import defaultdict, deque
from typing import List
from typing_extensions import DefaultDict

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q = deque([1])
        currTime = 0
        res = -1
        visitTimes = defaultdict(list)
        while q:
            for i in range(len(q)):
                node  = q.popleft()
                if node == n:
                    if res != -1:
                        return currTime
                    res = currTime
                for neighbor in adj[node]:
                    neiTimes = visitTimes[neighbor]
                    if len(neiTimes) == 0 or (len(neiTimes) == 1 and neiTimes[0] != currTime):
                        q.append(neighbor)
                        neiTimes.append(currTime)
            if (currTime // change) % 2 == 1:
                currTime += change - (currTime % change)
            currTime += time
        return res
