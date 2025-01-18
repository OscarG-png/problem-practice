from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1,0]
        }
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)]) # row, column, cost
        minCost = { (0, 0): 0 } # (r, c) => min cost

        while q:
            r, c, cost = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost

            for d in directions:
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc
                nCost = cost if d == grid[r][c] else cost + 1
                if (
                    nr < 0 or nc < 0 or
                    nr == ROWS or nc == COLS or
                    nCost >= minCost.get((nr, nc), float('inf'))
                ):
                    continue

                minCost[(nr, nc)] = nCost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, nCost))
                else:
                    q.append((nr, nc, nCost))
