class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            elif stack:
                curr = stack.pop()
                if p == ")" and curr != "(":
                    return False
                elif p == "]" and curr != "[":
                    return False
                elif p == "}" and curr != "{":
                    return False
            else:
                return False
        
        if not stack:
            return True
        else:
            return False
