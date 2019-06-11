class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        for num in nums:
            self.find_permute(nums, [num], set([num]), output)
        return output
    
    def find_permute(self, nums, arr, visited, permutations):
        if len(arr) == len(nums):
            permutation = arr[:]
            permutations.append(permutation)
        else:
            for num in nums:
                if num not in visited:
                    arr.append(num)
                    visited.add(num)
                    self.find_permute(nums, arr, visited, permutations)
                    visited.remove(num)
                    arr.pop()
