class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == len(B):
            if B in A + A:
                return True
            else :
                return False
