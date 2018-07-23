class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        maxdist = 0
        pre = 0
        binned = bin(N)[2:]
        
        for i in range(len(binned)):
            if binned[i] == '1':
                maxdist = max(maxdist, i - pre)
                pre = i
        
        return maxdist
