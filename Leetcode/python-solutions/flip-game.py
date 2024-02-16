class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []

        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                l = list(currentState)
                l[i] = '-'
                l[i + 1] = '-'
                res.append(''.join(l))
        return res
