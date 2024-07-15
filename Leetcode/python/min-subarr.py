class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        stack = []
        sumMin = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i

                count = (mid - left) * (right - mid) % MOD

                sumMin += (count * arr[mid]) % MOD
                sumMin %= MOD
            stack.append(i)
        return int(sumMin)
