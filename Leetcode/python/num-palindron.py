class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numStr = str(x)
        return numStr == numStr[::-1]
