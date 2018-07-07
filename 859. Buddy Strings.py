class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        count = 0
        diffA, diffB = [], []

        for i in range(len(A)):
            if A[i] != B[i]:
                diffA.append(A[i])
                diffB.append(B[i])
                count += 1
        
        if count == 2:
            return diffA[::-1] == diffB
        elif count == 0:
            return len(set(A)) < len(A)
        else:
            return False
