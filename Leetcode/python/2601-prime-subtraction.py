from math import sqrt
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(n):
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True

        prev = 0
        for n in nums:
            upperBound = n - prev
            largestPrime = 0
            for i in reversed(range(2, upperBound)):
                if isPrime(i):
                    largestPrime = i
                    break
            if n - largestPrime <= prev:
                return False
            prev = n - largestPrime
        return True
