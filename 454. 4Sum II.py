from collections import defaultdict
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = defaultdict(int)
        CD = defaultdict(int)
        count = 0
        
        for a in A:
            for b in B:
                AB[a + b] += 1
        
        for c in C:
            for d in D:
                CD[c + d] += 1
        
        for pair in AB:
            if -pair in CD:
                count += AB[pair] * CD[-pair]

        return count
