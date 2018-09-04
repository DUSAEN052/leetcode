class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = [letter.lower() for letter in s if letter.isalnum()]
        
        return cleaned == cleaned[::-1]
