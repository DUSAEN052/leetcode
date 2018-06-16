class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        if x < 0:
            output = - int(str(-x).rstrip('0')[::-1])
        else:
            output = int(str(x).rstrip('0')[::-1])
        
        if output < -2147483648 or output > 2147483647:
            return 0
        else:
            return output
