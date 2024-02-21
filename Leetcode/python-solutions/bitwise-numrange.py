class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        common_bits = 0

        while left != right:
            left >>= 1
            right >>= 1
            common_bits += 1
        return left << common_bits
