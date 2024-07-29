from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for m in range(1, len(rating) - 1):
            leftSmaller = rightLarger = 0

            for i in range(m):
                if rating[i] < rating[m]:
                    leftSmaller += 1
            for i in range(m + 1, len(rating)):
                if rating[i] > rating[m]:
                    rightLarger += 1
            res += leftSmaller * rightLarger
            leftLarger = m - leftSmaller
            rightSmaller = len(rating) - m - 1 - rightLarger
            res += leftLarger * rightSmaller

        return res
