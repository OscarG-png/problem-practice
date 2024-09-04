from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, d = 0, 0, 0
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        maxDistance = 0
        obstacles = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d - 1) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + directions[d][0], y + directions[d][1]
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
                    maxDistance = max(maxDistance, x * x + y * y)
        return maxDistance
