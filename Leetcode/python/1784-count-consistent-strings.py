from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowedSet = set(allowed)

        for word in words:
            if all(char in allowedSet for char in word):
                res += 1

        return res
