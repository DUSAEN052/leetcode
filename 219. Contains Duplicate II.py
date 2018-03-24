class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hmap = collections.defaultdict(list)
        i = 0
        
        for integer in nums:
            hmap[integer].append(i)
            if (hmap[integer]):
                for num in range(len(hmap[integer])):
                    if abs(hmap[integer][num] - i) <= k and abs(hmap[integer][num] - i) != 0:
                        return True
            i += 1

        return False
