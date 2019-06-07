class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        output = 0
        
        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                output += 1
        
        return output
