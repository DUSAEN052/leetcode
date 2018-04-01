# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        
        while low < high:
            mid = low + (high - low) / 2
            
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not isBadVersion(mid) and isBadVersion(mid + 1):
                return mid + 1
            elif not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid - 1
                
        return low
