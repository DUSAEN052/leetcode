class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        
        output = 0
        count = 0
        i = 1

        while i < len(A) - 1:
            if A[i] - A[i - 1] == A[i + 1] - A[i]:
                count += 1
                output += count
            else:
                count = 0
            i += 1

        return output
