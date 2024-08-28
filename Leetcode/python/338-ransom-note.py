class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = {}

        for c in magazine:
            magazineMap[c] = magazineMap.get(c, 0) + 1

        for l in ransomNote:
            if l not in magazineMap:
                return False
            else:
                if magazineMap[l] == 1:
                    magazineMap.pop(l)
                else:
                    magazineMap[l] -= 1
        return True
