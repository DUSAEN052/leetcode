class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []

        for i in range(len(A[0])):
            tmp = []

            for a in A:
                tmp.append(a[i])
            
            output.append(tmp)

        return output
