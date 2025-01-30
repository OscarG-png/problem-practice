from collections import defaultdict, deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def getConnectedComponent(src):
            q = deque([src])
            component = set([src])
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in component:
                        continue
                    q.append(nei)
                    component.add(nei)
                    visit.add(nei)
            return component

        def longestPath(src):
            q = deque([(src, 1)])
            dist = { src: 1 }

            while q:
                node, length = q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return -1
                        continue
                    q.append((nei, length + 1))
                    dist[nei] = length + 1
            return max(dist.values())

        visit = set()
        res = 0
        for i in range(1, n + 1):
            if i in visit:
                continue
            visit.add(i)
            component = getConnectedComponent(i)

            maxCount = 0
            for src in component:
                length = longestPath(src)
                if length == -1:
                    return -1

                maxCount = max(maxCount, length)
            res += maxCount
        return res
