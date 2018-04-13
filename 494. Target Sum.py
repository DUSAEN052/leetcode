class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def arrange(nums, current, hm, count, target):
            if current == len(nums):
                return 1 if count == target else 0
            elif (current, count) in hm:
                return hm[(current, count)]
            
            plus = arrange(nums, current + 1, hm, count + nums[current], target)
            minus = arrange(nums, current + 1, hm, count - nums[current], target)
            total = plus + minus
            hm[(current, count)] = total
            
            return total
        
        return arrange(nums, 0, {}, 0, S)
