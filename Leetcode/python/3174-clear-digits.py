class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        for item in s:
            if item.isdigit():
                res.pop()
            else:
                res.append(item)

        return ''.join(res)
