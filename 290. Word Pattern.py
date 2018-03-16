class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        letters = [] #letters from pattern
        words = [] #unique words
        sentence = str.split() #each word
        mapping = {}
        
        for word in sentence:
            if word not in words:
                words.append(word)
        
        for letter in pattern:
            if letter not in letters:
                letters.append(letter)
        
        if len(words) != len(letters) or len(sentence) != len(pattern):
            return False
        
        for word in words:
            if word not in mapping:
                mapping[word] = letters.pop(0)
        
        for i in range(len(sentence)):
            if mapping[sentence[i]] != pattern[i]:
                return False
        
        return True
