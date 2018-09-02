from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        output = []
        a, b, = set(A.split()), set(B.split())
        a_count = Counter(A.split())
        b_count = Counter(B.split())
        
        for ac in a_count:
            if a_count[ac] == 1:
                if ac not in b:
                    output.append(ac)
        
        for bc in b_count:
            if b_count[bc] == 1:
                if bc not in a:
                    output.append(bc)
        
        return output
