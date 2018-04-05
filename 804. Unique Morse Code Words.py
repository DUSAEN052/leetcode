class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transform = set()
        
        for word in words:
            gen = ""
            
            for i in range(len(word)):
                gen = gen + code[ord(word[i]) - ord('a')]
            
            transform.add(gen)
        
        return len(transform)
