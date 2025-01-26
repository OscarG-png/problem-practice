from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)
        longestCycle = 0
        visit = [False] * N

        length2Cycle= []
        for i in range(N):
            if visit[i]:
                continue
            start, cur = i, i
            curSet = set()

            while not visit[cur]:
                visit[cur] = True
                curSet.add(cur)
                cur = favorite[cur]

            if cur in curSet:
                length = len(curSet)
                while start != cur:
                    length -= 1
                    start = favorite[start]
                longestCycle = max(longestCycle, length)
                if length == 2:
                    length2Cycle.append([cur, favorite[cur]])

        inverted = defaultdict(list)
        for dst, src in enumerate(favorite):
            inverted[src].append(dst)

        def bfs(src, parent):
            q = deque([(src, 0)])
            maxLength = 0

            while q:
                node, length = q.popleft()
                if node == parent:
                    continue
                maxLength = max(maxLength, length)
                for nei in inverted[node]:
                    q.append((nei, length + 1))
            return maxLength

        chain_sum = 0
        for n1, n2 in length2Cycle:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chain_sum, longestCycle)
