class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''.join(str(n) for n in digits)
        num = int(num) + 1
        output = []
        
        for digit in str(num):
            output.append(int(digit))
        
        return output
