class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        output = []
        pdict = {}
        patt = len(set(pattern))
        
        for word in words:
            if len(word) == len(pattern) and len(set(word)) == patt:
                for i, j in zip(pattern, word):
                    pdict[i] = j
                
                for i in range(len(word)):
                    if pdict[pattern[i]] != word[i]:
                        pdict = {}
                        break
                
                if pdict:
                    output.append(word)
                    pdict = {}
        
        return output
