class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        output = 0
        xb = str(bin(x)[2:])
        yb = str(bin(y)[2:])
        
        if len(xb) < len(yb):
            xb = "0" * (len(yb) - len(xb)) + xb
        else:
            yb = "0" * (len(xb) - len(yb)) + yb
        
        for i in range(len(xb)):
            if xb[i] != yb[i]:
                output += 1

        return output
