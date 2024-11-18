from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        l = 0
        currSum = 0
        for r in range(N + abs(k)):
            currSum += code[r % N]

            if r - l + 1 > abs(k):
                currSum -= code[l % N]
                l = (l + 1) % N

            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % N] = currSum
                elif k < 0:
                    res[(r + 1) % N] = currSum
        return res
