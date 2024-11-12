from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [0] * len(queries)
        maxBeauty = 0
        j = 0
        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                maxBeauty = max(maxBeauty, items[j][1])
                j += 1
            res[i] = maxBeauty

        return res
