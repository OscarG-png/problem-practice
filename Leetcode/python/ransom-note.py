class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = {}

        for char in magazine:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        for char in ransomNote:
            if char in letters and letters[char] > 0:
                letters[char] -= 1
            else:
                return False
        return True
