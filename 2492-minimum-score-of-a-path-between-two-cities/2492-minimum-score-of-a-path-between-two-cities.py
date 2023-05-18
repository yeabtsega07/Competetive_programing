class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        class UnionFind:
            def __init__(self, size):
                self.root = { i:i for i in range ( size ) }
                self.rank = [0] * size
                self.size = size

            def find(self, member):

                if member != self.root[member]:
                    self.root[member] = self.find(self.root[member])
                
                return self.root[member]

            def union(self, x, y):
                
                rootX = self.find(x)
                rootY = self.find(y)
                
                if rootX != rootY:
                    
                    if self.rank[rootX] > self.rank[rootY]:
                        
                        self.root[rootY] = rootX
                        
                    elif self.rank[rootX] < self.rank[rootY]:
                        
                        self.root[rootX] = rootY
                        
                    else:
                        
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1


            def connected(self, x, y):
                return self.find(x) == self.find(y)
            
        check = UnionFind(n)

        for i, j, dis in roads:
            
            check.union(i - 1,j - 1)

        
        
        result = float("inf")
        for i, j, dis in roads:
            
            if check.connected(i - 1,0) or check.connected(i - 1, n - 1):
                result = min(result, dis)
            
               
            
        
        return result