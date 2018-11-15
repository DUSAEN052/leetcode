class RecentCounter:

    def __init__(self):
        self.lst = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.lst.append(t)
        
        while t - self.lst[0] > 3000:
            self.lst.pop(0)
        return len(self.lst)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
