class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""

        while columnNumber > 0:
            result = chr((columnNumber - 1) % 26 + ord("A")) + result
            columnNumber = (columnNumber - 1) // 26
        return result
