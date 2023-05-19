class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
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
                return self.root[x] == self.root[y]
        
        n = len(stones)
        check = UnionFind(n)
        track = defaultdict(list)
        for i, loc in enumerate(stones):
            
            track[i] = loc
        
        for i in range(n):
            
            for j in range(n):
                
                if i != j:
                    if track[i][1] == track[j][1] or track[i][0] == track[j][0]:
                        
                        check.union(i,j)
        
        count = 0
        for i in range(n):
            
            if check.root[i] == i:
                count += 1
        
        return n - count
            
            
        
                
            
        