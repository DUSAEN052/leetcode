class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stck, count = 0, 0
        
        for s in S:
            if s == '(':
                stck += 1
            elif s == ')' and not stck:
                count += 1
            else:
                stck -= 1
        
        return count + stck     
