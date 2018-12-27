class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def find(arr, target, index, curr, solution):
            if target == 0:
                solution.append(curr[:])
                return
            elif 0 > target:
                return
            
            for i in range(index, len(arr)):
                curr.append(arr[i])
                find(arr, target - candidates[i], i, curr, solution)
                curr.pop()
        
        solution = []
        
        for i in range(len(candidates)):
            find(candidates, target - candidates[i], i, [candidates[i]], solution)
        
        return solution
