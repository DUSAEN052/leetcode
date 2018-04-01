class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        
        if words:
            size = len(words.pop())
            return size
        else:
            return 0
