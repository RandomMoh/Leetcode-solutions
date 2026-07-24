class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for t in tokens:
            # Check if it's an operator
            if t in {"+", "-", "*", "/"}:
                b, a = stack.pop(), stack.pop()
                
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    # int(a / b) perfectly handles truncation toward zero in Python
                    stack.append(int(a / b))
            else:
                # It's a number
                stack.append(int(t))
                
        return stack[0]