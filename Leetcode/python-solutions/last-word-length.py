class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(' ')
        words = [
            word for word in words if word
        ]
        if not words:
            return 0

        return len(words[-1])


# surprised this did really good on runtime and memory.
