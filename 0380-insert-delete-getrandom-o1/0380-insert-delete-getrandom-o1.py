class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.set = []

    def insert(self, val: int) -> bool:
        if val not in self.index:
            self.index[val] = len(self.set)
            self.set.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.index:
            val_idx = self.index[val]
            self.index[self.set[-1]] = val_idx
            self.set[val_idx],self.set[-1] = self.set[-1],self.set[val_idx]
            self.set.pop()
            self.index.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()