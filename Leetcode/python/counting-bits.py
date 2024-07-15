class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
