class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        A.append([0] * len(A[0]))
        
        for row in A:
            row.append(float("inf"))

        for i in range(1, len(A)):
            for k in range(len(A[0])):
                if k == 0:
                    A[i][k] += min(A[i - 1][k], A[i - 1][k + 1])
                elif k == len(A[0]) - 1:
                    A[i][k] += min(A[i - 1][k], A[i - 1][k - 1])
                else:
                    A[i][k] += min(A[i - 1][k], A[i - 1][k - 1], A[i - 1][k + 1])
                
        return min(A[-1])
