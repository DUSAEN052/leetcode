class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.find_permute(nums, [], set(), output)
        return output
    
    def find_permute(self, nums, arr, visited, permutations):
        if len(arr) == len(nums):
            permutations.append(arr[:])
        else:
            for num in nums:
                if num not in visited:
                    arr.append(num)
                    visited.add(num)
                    self.find_permute(nums, arr, visited, permutations)
                    visited.remove(num)
                    arr.pop()