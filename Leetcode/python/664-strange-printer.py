class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return self.helper(0, n - 1, s, dp)

    def helper(self, i: int, j: int, s: str, dp: list) -> int:
        if i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        firstLetter = s[i]

        ans = 1 + self.helper(i + 1, j, s, dp)
        for k in range(i + 1, j + 1):
            if s[k] == firstLetter:
                betterAns = self.helper(i, k - 1, s, dp) + self.helper(k + 1, j, s, dp)
                ans = min(ans, betterAns)
        dp[i][j] = ans
        return ans
