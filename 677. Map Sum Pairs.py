class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.mapping[key] = val
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        output = 0
        
        for key in self.mapping:
            if key.startswith(prefix):
                output += self.mapping[key]
        
        return output


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
