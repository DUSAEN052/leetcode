class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        
        while True:
            count = 0
            
            for num in str(n):
                count += int(num) * int(num)
            
            if count in visited:
                return False
            else:
                if count == 1:
                    return True
                
                visited.add(count)
                n = count
