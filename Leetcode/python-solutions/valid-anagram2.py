class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS = {}
        for char in s:
            hashS[char] = hashS.get(char, 0) + 1

        hashT = {}
        for char in t:
            hashT[char] = hashT.get(char, 0) + 1

        return hashS == hashT

# refactored solution that has a better runtime than my previous solution
