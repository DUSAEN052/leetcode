from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pLen = len(p)
        pCount = Counter(p)
        currCount = Counter(s[:pLen - 1])
        output = []
        
        for i in range(len(s) - pLen + 1):
            index = i + pLen - 1
            
            if s[index] in currCount:
                currCount[s[index]] += 1
            else:
                currCount[s[index]] = 1
            
            if pCount == currCount:
                output.append(i)
            
            currCount[s[i]] -= 1
            
            if currCount[s[i]] == 0:
                del currCount[s[i]]
        
        return output
