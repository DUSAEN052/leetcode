from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        convLP = ""
        sortedWords = sorted(words, key=len)
        
        for letter in licensePlate:
            if letter.isalpha():
                convLP += letter.lower()
        
        countedLP = Counter(convLP)
        
        for word in sortedWords:
            cword = Counter(word)
            count = 0
            
            for counted in countedLP:
                if counted in cword:
                    if cword[counted] >= countedLP[counted]:
                        count += 1
                if count == len(countedLP):
                    return word
