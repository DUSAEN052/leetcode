class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transform = set()
        
        for word in words:
            gen = ''.join([code[ord(word[i]) - ord('a')] for i in range(len(word))])
            transform.add(gen)
        
        return len(transform)
