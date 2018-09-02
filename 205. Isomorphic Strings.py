class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in mapping:
                if t[i] != mapping[s[i]]:
                    return False
            elif t[i] in mapping.values():
                return False
            else:
                mapping[s[i]] = t[i]
        
        return True
