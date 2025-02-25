from typing import List


class Solution:
  def numOfSubarrays(self, arr: List[int]) -> int:
    prefixSum = 0
    oddCount = 0
    evenCount = 0
    res = 0
    MOD = 10**9 + 7

    for n in arr:
        prefixSum += n

        # odd case
        if prefixSum % 2:
            res = (res + 1 + evenCount) % MOD
            oddCount += 1
        # even case
        else:
            res = (res + oddCount) % MOD
            evenCount += 1

    return res
