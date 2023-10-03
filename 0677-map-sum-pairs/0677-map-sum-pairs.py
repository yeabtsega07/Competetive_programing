class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.isEnd = False


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.track = {}
        
        
    def insert(self, key: str, val: int) -> None:
        cur = self.root
        curVal = val
        
        if key in self.track:
            curVal = val - self.track[key]

        
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur  = cur.children[char]
            cur.count += curVal
            
        cur.isEnd = True 
        self.track[key] = val
        

    def sum(self, prefix: str) -> int:
        cur  = self.root
        res = 0
        
        for char in prefix:
            if char not in cur.children:
                return res
            cur = cur.children[char]
        
        res += cur.count
        return res
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)