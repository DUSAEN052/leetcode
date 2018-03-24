class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                l , r = list(s), list(s)
                del l[left]
                del r[right]

                if l[::-1] == l or r[::-1] == r:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        
        return True
