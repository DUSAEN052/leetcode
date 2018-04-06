class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if newColor == image[sr][sc]:
            return image
        
        def flood(image, sr, sc, newColor, oldColor):
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            
            if sc >= 0 and sc < len(image[0]) and sr >= 0 and sr < len(image):
                if image[sr][sc] == oldColor:
                    image[sr][sc] = newColor

                    for dire in dirs:
                        flood(image, sr + dire[0], sc + dire[1], newColor, oldColor)
        
        flood(image, sr, sc, newColor, image[sr][sc])
        
        return image
