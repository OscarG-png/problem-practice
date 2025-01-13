class Solution:
    def minimumLength(self, s: str) -> int:
        charFrequency = [0] * 26
        totalLength = 0

        for char in s:
            charFrequency[ord(char) - ord('a')] += 1

        for frequency in charFrequency:
            if frequency == 0:
                continue
            if frequency % 2 == 0:
                totalLength += 2
            else:
                totalLength += 1

        return totalLength
