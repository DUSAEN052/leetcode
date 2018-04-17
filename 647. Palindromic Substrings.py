class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def build(s, left, right):
            total = 0
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    total += 1
                    left -= 1
                    right += 1
                else:
                    break
            
            return total
        
        total = 0
        
        for i in range(len(s)):
            total += build(s, i, i) + build(s, i, i + 1)
        
        return total
