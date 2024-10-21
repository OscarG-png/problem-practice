class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def dfs(i, currSet):
            if i == len(s):
                return 0

            res = 0
            for j in range(i, len(s)):
                subStr = s[i:j + 1]
                if subStr in currSet:
                    continue
                currSet.add(subStr)
                res = max(res, dfs(j + 1, currSet) + 1)
                currSet.remove(subStr)

            return res
        return dfs(0, set())
