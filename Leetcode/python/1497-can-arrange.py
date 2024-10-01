from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainderCount = {}

        for num in arr:
            remainder = num % k

            if remainder < 0:
                remainder += k
            if remainder in remainderCount:
                remainderCount[remainder] += 1
            else:
                remainderCount[remainder] = 1

        for rem in remainderCount:
            if rem == 0:
                if remainderCount[rem] % 2 != 0:
                    return False
            elif rem * 2 == k:
                if remainderCount[rem] % 2 != 0:
                    return False
            else:
                if remainderCount[rem] != remainderCount.get(k - rem, 0):
                    return False
        return True
