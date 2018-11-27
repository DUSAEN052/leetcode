class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stck = []
        count = 0
        
        for s in S:
            if s == '(':
                stck.append(s)
            else:
                if not stck:
                    count += 1
                else:
                    stck.pop()
        
        return count + len(stck)     
