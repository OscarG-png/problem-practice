class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        n = min(len(word1), len(word2))
        for i in range(n):
            result += word1[i] + word2[i]
        result += word1[n:] + word2[n:]
        return result

# runtime wasn't as fast as other submissions and memory usage is okay.
# I'm happy with how simple the code looks though.
