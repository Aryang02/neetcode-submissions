class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['*', '+', '-', '/']
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token in ops:      
                b = stack.pop()
                a = stack.pop()  
                if token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
                elif token == "+":
                    stack.append(a+b)
                else:
                    stack.append(a-b)
            else:
                stack.append(int(token))
        return stack[-1]
                