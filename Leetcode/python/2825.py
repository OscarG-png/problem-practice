class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        targetI, targetLen = 0, len(str2)
        for currChar in str1:
            if targetI < targetLen:
                # Check if currChar can be transformed to str2[targetI]
                if currChar == str2[targetI] or (chr((ord(currChar) - ord('a') + 1) % 26 + ord('a')) == str2[targetI]):
                    targetI += 1
        return targetI == targetLen
