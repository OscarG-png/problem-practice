class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev1, prev2 = 1, 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        return prev2


# improved runtime and memory usage from previous submission
