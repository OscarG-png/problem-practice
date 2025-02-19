class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2**(n - 1))

        res = []
        choices = 'abc'
        left, right = 1, total_happy

        for i in range(n):
            curr = left
            partitionSize = (right - left + 1) // len(choices)

            for c in choices:
                if k in range(curr, curr + partitionSize):
                    res.append(c)
                    left = curr
                    right = curr + partitionSize - 1
                    choices = 'abc'.replace(c, '')
                    break
                curr += partitionSize

        return ''.join(res)
