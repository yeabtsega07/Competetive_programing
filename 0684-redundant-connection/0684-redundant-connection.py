class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        class UnionFind:
            def __init__(self, size):
                self.root = { i:i for i in range ( size ) }
                self.rank = [0] * size
                self.size = size

            def find(self, member):

                root = member
                while root != self.root[root]:
                    root = self.root[root]

                while member != root:
                    parent = self.root[member]
                    self.root[member] = root
                    member = parent

                return root

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
        redundants = []
        for i, j in edges:
            if not check.connected(i - 1,j - 1):
                check.union(i - 1,j - 1)
            else:
                redundants.append([i,j])
        
        return redundants[-1]
        
        

            
        