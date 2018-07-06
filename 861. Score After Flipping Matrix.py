class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        output = 0
        numbers = [0] * len(A[0])

        for i in range(len(A)):
            if A[i][0] == 0:
                A[i] = [1 - A[i][x] for x in range(len(A[i]))]

            for j in range(len(A[i])):
                if A[i][j] == 1:
                    numbers[j] += 1

        for i in range(len(A[0])):
            if numbers[i] <= len(A) // 2:

                for k in range(len(A)):
                    A[k][i] = 1 - A[k][i]

        for i in A:
            output += (int(''.join(str(item) for item in i), 2))

        return output
