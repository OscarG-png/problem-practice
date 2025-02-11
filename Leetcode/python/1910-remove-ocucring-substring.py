class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        partLength = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= partLength and ''.join(stack[-partLength:]) == part:
                del stack[-partLength:]

        return ''.join(stack)
