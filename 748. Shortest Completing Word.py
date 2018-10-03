from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        sortedWords = sorted(words, key=len)
        convLP = "".join([letter.lower() for letter in licensePlate if letter.isalpha()])
        countedLP = Counter(convLP)
        
        for word in sortedWords:
            cword = Counter(word)
            count = 0
            
            for counted in countedLP:
                if counted in cword and cword[counted] >= countedLP[counted]:
                    count += 1
                if count == len(countedLP):
                    return word
