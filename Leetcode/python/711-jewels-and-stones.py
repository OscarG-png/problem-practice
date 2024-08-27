class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        jewelMap = {}

        for c in jewels:
            jewelMap[c] = jewelMap.get(c, 0)

        for c in stones:
            if c in jewelMap:
                jewelMap[c] += 1

        for key in jewelMap.keys():
            res += jewelMap[key]

        return res
