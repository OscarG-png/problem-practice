from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        n = len(senate)

        rStack, dStack = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                rStack.append(i)
            else:
                dStack.append(i)
        while rStack and dStack:
            currR = rStack.popleft()
            currD = dStack.popleft()

            if currR < currD:
                rStack.append(currD + n)
            else:
                dStack.append(currR + n)

        return "Radiant" if rStack else "Dire"
