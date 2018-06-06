from collections import Counter
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        output = len(candies) // 2 
        candy = set(candies)
        candy_count = len(candy)
        
        return output if candy_count > output else candy_count
