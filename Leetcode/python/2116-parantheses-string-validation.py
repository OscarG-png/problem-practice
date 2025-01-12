class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        lockedStack = []
        unlockedStack = []

        for i in range(len(s)):
            if locked[i] == '0':
                unlockedStack.append(i)
            elif s[i] == "(":
                lockedStack.append(i)
            else:
                if lockedStack:
                    lockedStack.pop()
                elif unlockedStack:
                    unlockedStack.pop()
                else:
                    return False

        while lockedStack and unlockedStack and lockedStack[-1] < unlockedStack[-1]:
            lockedStack.pop()
            unlockedStack.pop()
        if lockedStack:
            return False
        return True
