class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        string = strs[0]
        
        for s in range(1, len(strs)):
            while len(string) > 0:
                if strs[s].startswith(string):
                    break
                else:
                    string = string[:-1]
        return string
