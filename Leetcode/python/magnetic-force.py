class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        l, r = 1, position[-1] - position[0]
        res = -1

        while l <= r:
            mid = l + (r - l) // 2
            lastPosition, balls = position[0], 1

            for i in range(1, len(position)):
                if position[i] - lastPosition >= mid:
                    lastPosition = position[i]
                    balls += 1

            if balls >= m:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
