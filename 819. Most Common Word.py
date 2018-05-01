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
        
        counted = {k : v for k,v in counted.items() if k not in banned}
        
        return max(counted, key=counted.get)
