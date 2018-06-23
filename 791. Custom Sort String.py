from collections import Counter
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        order = {}
        output = []
        t = Counter(T)
        
        for i, letter in enumerate(S, 0):
            order[i] = letter
        
        output = [order[i] * t[order[i]] for i in range(len(order))]
        
        for letter in T:
            if letter not in S:
                output.append(letter)
        
        return ''.join(c for c in output)
