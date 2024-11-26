from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src, dst in edges:
            incoming[dst] += 1

        champions = []

        for i, inc_count in enumerate(incoming):
            if not inc_count:
                champions.append(i)
        if len(champions) > 1:
            return -1
        return champions[0]
