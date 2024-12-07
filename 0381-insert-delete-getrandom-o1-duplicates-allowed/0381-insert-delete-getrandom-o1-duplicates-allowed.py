class RandomizedCollection:

    def __init__(self):
        self.index = defaultdict(set)
        self.set = []

    def insert(self, val: int) -> bool:
        self.index[val].add(len(self.set))
        self.set.append(val)
        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.index[val]:
            return False
        last = self.set[-1]
        index = self.index[val].pop()
        
        self.set[index] = last
        self.index[last].add(index)
        
        self.index[last].discard(len(self.set) - 1)
        self.set.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.set)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()