class OrderedStream:

    def __init__(self, n: int):
        
        self.track = defaultdict(str)
        self.top = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.track[idKey] = value
        res = []
        
        while self.track[self.top]:
            res.append(self.track.pop(self.top))
            self.top += 1
        
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
"""
1 - a
2 - 
3 - c

1

"""