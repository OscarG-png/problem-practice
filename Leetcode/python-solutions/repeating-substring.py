class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        # we don't need to loop through the entire string
        for i in range(1, n // 2 + 1):
            # we check if the string is divisible by i
            # and if a substring repeated is equal to the string
            if n % i == 0 and s[:i] * (n // i) == s:
                return True
        return False
