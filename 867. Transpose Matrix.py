class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []

        for i in range(len(A[0])):
            tmp = [a[i] for a in A]
            output.append(tmp)

        return output
