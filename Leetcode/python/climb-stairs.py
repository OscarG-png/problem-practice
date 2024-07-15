class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev1, prev2 = 0, 1

        for i in range(n):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        return prev2

# improved my solution again.
