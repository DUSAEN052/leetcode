class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = [a for a in A if a % 2 != 0]
        even = [a for a in A if a % 2 == 0]
        return [even.pop() if i % 2 == 0 else odd.pop() for i in range(len(A))]
