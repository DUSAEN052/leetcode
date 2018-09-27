class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = []
        b = []
        
        for num in A:
            if num % 2 == 0:
                a.append(num)
            else:
                b.append(num)
        
        return a + b
