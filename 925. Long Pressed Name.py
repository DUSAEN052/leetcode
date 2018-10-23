class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name == typed:
            return True
        
        nm, typ = [], []
        n = list(name)
        t = list(typed)
        
        while n:
            count = 0
            letter = n[0]
            
            if letter == n[0]:
                while n and letter == n[0]:
                    count += 1
                    n.pop(0)
            nm.append((letter, count))
        
        while t:
            count = 0
            letter = t[0]
            
            if letter == t[0]:
                while t and letter == t[0]:
                    count += 1
                    t.pop(0)
            typ.append((letter, count))
        
        if len(nm) != len(typ):
            return False
        
        for a, b in zip(nm, typ):
            if a[0] != b[0] or a[1] > b[1]:
                return False
        return True
