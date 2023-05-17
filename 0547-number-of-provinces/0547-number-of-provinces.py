class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        class UnionFind:
            def __init__(self, size):
                self.root = { i:i for i in range ( size ) }
                self.rank = [0] * size
                self.size = size

            def find(self, member):

                if member == self.root[member]:
                    return member
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
                return self.root[x] == self.root[y]
            
        check = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                
                if isConnected[i][j]:
                    check.union(i,j)
        
        parent = 0
        for i in range(len(isConnected)):
            if check.root[i] == i:
                parent += 1
        
        return parent

                