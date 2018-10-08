class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        r = ""
        cpy = list(S)
        
        for i in range(len(S)):
            if not S[i].isalpha():
                r += S[i]
            else:
                while not cpy[-1].isalpha():
                    cpy.pop()
                r += cpy.pop()
        
        return r
