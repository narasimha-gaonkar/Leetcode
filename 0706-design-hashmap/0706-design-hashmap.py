class MyHashMap:

    def __init__(self):
        
        self.size = 1000
        self.buckets = [None] * self.size
        

    def put(self, key: int, value: int) -> None:
        
        hash_key = key % self.size
        
        if self.buckets[hash_key] == None:
            
            self.buckets[hash_key] = []
        
        for idx, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                self.buckets[hash_key][idx] = (k ,value)
                return
        
        self.buckets[hash_key].append((key, value))
        return
        
        

    def get(self, key: int) -> int:
        
        hash_key = key % self.size
        
        if self.buckets[hash_key] == None:
            return -1
        
        for k, v in self.buckets[hash_key]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = key % self.size
        if self.get(key) != -1:
            for k, v in self.buckets[hash_key]:
                if k == key:
                    self.buckets[hash_key].remove((k, v))
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)