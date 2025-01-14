from typing import List


class Solution:
  def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
      n = len(A)
      res = [0] * n
      seenA, seenB = set(), set()
      commonCount = 0

      for i in range(n):
          seenA.add(A[i])
          seenB.add(B[i])

          if A[i] in seenB:
              commonCount += 1
          if B[i] in seenA and A[i] != B[i]:
              commonCount += 1

          res[i] = commonCount
      return res
