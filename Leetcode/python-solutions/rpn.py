class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-*/"
        for item in tokens:
            if item in operations:
                b = stack.pop()
                a = stack.pop()
                if item == '+':
                    stack.append(a + b)
                elif item == '-':
                    stack.append(a - b)
                elif item == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(item))
        return stack.pop()
