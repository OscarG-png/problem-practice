class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        maxAlt = 0
        for item in gain:
            alt += item
            maxAlt = max(maxAlt, alt)
        return maxAlt
