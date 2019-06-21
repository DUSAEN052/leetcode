class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        output = []
        words = text.split(' ')
        
        for i in range(0, len(words) - 2, 1):
            if words[i] == first and words[i + 1] == second:
                output.append(words[i + 2])
            
        return output
