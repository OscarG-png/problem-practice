from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        n = len(chalk)

        left = k % total
        if left == 0:
            return 0

        for i in range(n):
            left -= chalk[i]
            if left < 0:
                return i

        return -1
