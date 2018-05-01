from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        strp = [word.lower().strip("!?',;.") for word in paragraph.split()]
        counted = Counter(strp)
        
        for item in counted:
            if item in banned:
                counted[item] = 0
        
        return max(counted, key=counted.get)
