class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output = []
        
        def find(k, n, arr, total, curr):
            if k == 0 and total == n:
                output.append(arr)
                return
            elif k == 0:
                return
    
            for i in range(curr + 1, 10):
                newArr = arr[:] + [i]
                find(k - 1, n, newArr, total + i, i)
        
        for i in range(1, 10):
            find(k - 1, n, [i], i, i)
        
        return output
