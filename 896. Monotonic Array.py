class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = None
        
        for i in range(len(A) - 1):
            if increase == True:
                if A[i] > A[i + 1]:
                    return False
            elif increase == False:
                if A[i] < A[i + 1]:
                    return False
            else:
                k = 0
                
                while k < len(A) - 1 and A[k] == A[k + 1]:
                    k += 1
                
                if k == len(A) - 1:
                    return True
                i = k
                
                if A[k] < A[k + 1]:
                    increase = True
                else:
                    increase = False
        
        return True
