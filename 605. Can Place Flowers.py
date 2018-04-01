class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed.append(7)
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and i == 0 and flowerbed[i + 1] != 1:
                count += 1
            elif flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i + 1] = 5
                count += 1
            
            if flowerbed[i] == 5 and flowerbed[i + 1] == 1:
                count -= 1
        
        if count >= n:
            return True
        else:
            return False
