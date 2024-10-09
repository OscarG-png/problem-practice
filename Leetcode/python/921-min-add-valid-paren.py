class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openCount = 0
        res = 0

        for c in s:
            if c == "(":
                openCount += 1
            else:
                if openCount == 0:
                    res += 1
                openCount = max(openCount - 1, 0)


        return res + openCount
