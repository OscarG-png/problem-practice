from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, j in stones:
            graph[i].append((i, j))
            graph[~j].append((i, j))

        visited = set()
        groups = 0

        for i, j in stones:
            if (i, j) not in visited:
                groups += 1
                stack = [(i, j)]
                visited.add((i, j))

                while stack:
                    currI, currJ = stack.pop()

                    for newI, newJ in graph[currI]:
                        if (newI, newJ) not in visited:
                            stack.append((newI, newJ))
                            visited.add((newI, newJ))

                    for newI, newJ in graph[~currJ]:
                        if (newI, newJ) not in visited:
                            stack.append((newI, newJ))
                            visited.add((newI, newJ))

        return len(stones) - groups
