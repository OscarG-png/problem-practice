from typing import List
from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)

        for row in matrix:
            rowKey = tuple(row)
            if row[0]:
                rowKey = tuple([0 if n else 1 for n in row])

            count[rowKey] += 1

        return max(count.values())
