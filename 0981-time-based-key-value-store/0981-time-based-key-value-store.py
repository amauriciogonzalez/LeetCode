class TimeMap(object):

    def __init__(self):
        self.map = {} # a map where the keys are [val, timestamp]
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        def binarySearch(i, j, result):
            if i > j:
                return result
            midpoint = int(float(i + j) / 2)
            value = self.map[key][midpoint][1]
            if value <= timestamp:
                result = self.map[key][midpoint][0]
                return binarySearch(midpoint + 1, j, result)
            else:
                return binarySearch(i, midpoint - 1, result)
        return binarySearch(0, len(self.map.get(key, [])) - 1, "")
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)