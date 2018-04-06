class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        
        while True:
            count = sum([int(num) * int(num) for num in str(n)])
            
            if count in visited:
                return False
            elif count == 1:
                return True
            else:
                visited.add(count)
                n = count
