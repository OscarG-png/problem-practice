class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startNum = bin(start)[2:]
        endNum = bin(goal)[2:]
        maxLen = max(len(startNum), len(endNum))

        startNum = startNum.zfill(maxLen)
        endNum = endNum.zfill(maxLen)

        res = 0
        for s, e in zip(startNum, endNum):
            if s != e:
                res += 1

        return res
