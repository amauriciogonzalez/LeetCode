class LRUCache(object):

    # Popular interview question!

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Return -1 if key is not in cache. Otherwise, return the value, but first move the key to the end
        # of the dictionary.
        if key not in self.cache:
            return -1
        else:
            self.cache[key] = self.cache.pop(key)
        return self.cache[key]        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if the key is not in the cache and we are at capacity, pop the least recently used key, or rather
        # the first item in the dictionary. Otherwise update the key and bring it to the front of the
        # dictionary.
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        else:
            self.cache.pop(key)
        self.cache[key] = value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)