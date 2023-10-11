class MyHashMap:

    def __init__(self):
        
        self.hash_map = []

    def put(self, key: int, value: int) -> None:
        
        for i, cur in enumerate(self.hash_map):

            key_, val = cur
            if key_ == key:
                self.hash_map[i] = (key, value)
                return
        
        self.hash_map.append((key, value))

    def get(self, key: int) -> int:
        
        for key_, val in self.hash_map:
            if key_ == key:
                return val
        return -1

    def remove(self, key: int) -> None:
        
        for i, cur in enumerate(self.hash_map):
            key_, val = cur
            if key_ == key:

                self.hash_map.remove((key_, val))

                break
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)