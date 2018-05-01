class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        output = ""
        vowel = {'a', 'e', 'i', 'o', 'u'}
        
        for i, word in enumerate(S.split(), 1):
            if word[0].lower() not in vowel:
                output += (word[1:] + word[0]) + "ma" + 'a' * i + " "
            else:
                output += word + "ma" + 'a' * i + " "
        
        return output[:-1]
