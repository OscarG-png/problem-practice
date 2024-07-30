class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        aCountRight = 0

        for c in s:
            aCountRight += 1 if c == "a" else 0

        bCountLeft = 0
        res = n
        for i, c in enumerate(s):
            if c == 'a':
                aCountRight -= 1
            res = min(res, bCountLeft + aCountRight)
            if c == 'b':
                bCountLeft += 1
        return res
