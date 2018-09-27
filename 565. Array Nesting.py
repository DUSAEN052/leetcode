class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        path = set()
        visited = set()
        
        for i in range(len(nums)):
            entry = nums[i]
            
            if entry not in visited:
                
                while entry not in path:
                    visited.add(entry)
                    path.add(entry)
                    entry = nums[entry]
                
                output = max(len(path), output)
                path = set()
        
        return output
