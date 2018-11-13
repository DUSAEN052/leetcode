class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        target = (sum(A) - sum(B)) // 2
        a = set(A)
        
        for number in B:
            value = number + target
            
            if value in a:
                return [value, number]
