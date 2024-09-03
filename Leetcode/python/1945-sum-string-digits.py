class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numStr = ''.join(str(ord(c) - 96) for c in s)

        res = 0
        for _ in range(k):
            res = sum(int(c) for c in numStr)
            numStr = str(res)
        return res
