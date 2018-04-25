class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        output = []
        cloca = [i for i, char in enumerate(S) if char == C]
        
        for j, char in enumerate(S):
            small = float("inf")
            
            for k, char in enumerate(cloca):
                small = min(small, abs(j - cloca[k]))
            
            output.append(small)
        
        return output
