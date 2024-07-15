class Solution:
    def confusingNumber(self, n: int) -> bool:
        numMap = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        res = 0
        num = n
        while n > 0:
            x = n % 10
            if x not in numMap:
                return False
            res = res * 10 + numMap[x]
            n //= 10
        return res != num
