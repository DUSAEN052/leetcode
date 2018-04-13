class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def arrange(nums, current, hm, count, target):
            if current == len(nums) and count == target:
                return 1
            elif current == len(nums) and count != target:
                return 0
            if (current, count) in hm:
                return hm[(current, count)]
            
            plus = arrange(nums, current + 1, hm, count + nums[current], target)
            minus = arrange(nums, current + 1, hm, count - nums[current], target)
            total = plus + minus
            hm[(current, count)] = total
            
            return total

        plus = 0
        plus += arrange(nums, 0, {}, 0, S)
        
        return plus
