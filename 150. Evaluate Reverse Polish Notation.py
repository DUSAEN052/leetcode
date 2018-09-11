class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for t in tokens:
            if t.isnumeric():
                stack.append(int(t))
            elif t[0] == "-" and len(t) > 1:
                stack.append(-int(t.lstrip("-")))
            else:
                x = stack.pop()
                y = stack.pop()
                
                if t == "+":
                    stack.append(x + y)
                elif t == "-":
                    stack.append(y - x)
                elif t == "*":
                    stack.append(x * y)
                elif t == "/":
                    stack.append(int(y / x))
            
        return sum(stack)
