class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10

        if carry:
            digits.insert(0, carry)
        return digits
