class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        number = ""
        op = "+"
        s = s.replace(" ", "")
        
        for chara in s + " ":
            if chara.isnumeric():
                number += chara
            else:
                if number:
                    number = int(number)

                if op == "+":
                    stack.append(number)
                elif op == "-":
                    stack.append(-1 * number)
                elif op == "*":
                    stack.append(stack.pop() * number)
                elif op == "/":
                    stack.append(int(stack.pop() / number))
                
                op = chara
                number = ""

        return sum(stack)
