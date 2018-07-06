class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        
        def generate(inpt, left, right, n):
            if len(inpt) == 2 * n:
                output.append(inpt)
                return
            
            if left < right and left < n:
                generate(inpt + ')', left + 1, right, n)
            
            if right < n:
                generate(inpt + '(', left, right + 1, n)
        
        generate("", 0, 0, n)
        return output
