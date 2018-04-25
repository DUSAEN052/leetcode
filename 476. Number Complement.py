class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binnum = bin(num)[2:]
        output = ''.join('1' if digit == '0' else '0' for digit in binnum)
        
        return int(output, 2)
