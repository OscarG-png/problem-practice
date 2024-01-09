class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        charCount = {}
        for char in s:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        for char in t:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        for key, value in charCount.items():
            if value % 2 == 1:
                return key
