from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for v1, v2, dist in edges:
            adj[v1].append((v2, dist))
            adj[v2].append((v1, dist))

        def dijkstra(src):
            heap = [(0, src)]
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                else:
                    visit.add(node)
                    for nei, dist2 in adj[node]:
                        neiDist = dist + dist2
                        if neiDist <= distanceThreshold:
                            heapq.heappush(heap, (neiDist, nei))
            return len(visit) - 1

        res, minCount = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count <= minCount:
                res, minCount = src, count
        return res
