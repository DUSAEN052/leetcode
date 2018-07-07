class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxlen = 0

        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                left, right = i, i
                leftc, rightc = 0, 0

                while left > 0 and A[left] > A[left - 1]:
                    leftc += 1
                    left -= 1

                while right < len(A) - 1 and A[right] > A[right + 1]:
                    rightc += 1
                    right += 1

                maxlen = max(maxlen, leftc + rightc + 1)

        return maxlen
