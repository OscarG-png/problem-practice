from collections import Counter


class Solution:
    def maximumLength(self, s: str) -> int:
        subArrays = []

        for i in range(len(s)):
            idx = i
            while idx < len(s) and s[idx] == s[i]:
                subArrays.append(s[i:idx + 1])
                idx += 1

        counter = Counter(subArrays)
        maxLen = 0

        for j, n in counter.items():
            if n >= 3:
                if len(j) > maxLen:
                    maxLen = len(j)

        if maxLen == 0:
            return -1
        return maxLen
