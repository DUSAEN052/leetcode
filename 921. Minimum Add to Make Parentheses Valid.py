class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stck = 0
        count = 0
        
        for s in S:
            if s == '(':
                stck += 1
            else:
                if not stck:
                    count += 1
                else:
                    stck -= 1
        
        return count + stck     
