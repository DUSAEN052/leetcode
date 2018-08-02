class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        output = ""
        
        for s in str:
            if 97 > ord(s) >= 65:
                output += chr(ord(s) + 32)
            else:
                output += s
        
        return output
