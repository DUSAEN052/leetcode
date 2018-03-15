class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = list(nums)
        group = []
        fz = 0
        lz = 0
        sub.sort()
        
        for i in range(len(nums)):
            if sub[i] == nums[i]:
                group.append(1)
            else:
                group.append(0)
        if 0 in group:
            for k in range(len(group)):
                if group[k] == 0:
                    fz = k
                    break
            for l in range(len(group) - 1, -1, -1):
                if group[l] == 0:
                    lz = l
                    break
            return lz - fz + 1
        else:
            return 0
            