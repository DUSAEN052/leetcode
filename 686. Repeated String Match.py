class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        count = 0
        a = A
        
        while len(a) <= len(B) + len(A) * 2:
            count += 1
            if B in a:
                return count
            a += A
            
        return -1
