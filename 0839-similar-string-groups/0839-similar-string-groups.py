class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        class UnionFind:
            def __init__(self, n, words):
                self.parent = [i for i in range(n)]
                self.size = [1 for i in range(n)]
                self.words = words
            
            def find(self, index):
                
                if self.parent[index] == index:
                    return index
                
                self.parent[index] = self.find(self.parent[index])
                return self.parent[index]
            
            def union(self, index1, index2):
                
                parent1, parent2 = self.find(index1), self.find(index2)
                
                if parent1 == parent2:
                    return
                
                if self.size[parent1] < self.size[parent2]:
                    parent1, parent2 = parent2, parent1
                    
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
                
                return
        
        obj = UnionFind(len(strs), strs)
        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                mis_match = []
                for x in range(len(strs[i])):
                    if strs[i][x] != strs[j][x]:
                        mis_match.append(x)
                    if len(mis_match) > 2:
                        break
                
                if not mis_match:
                    obj.union(i, j)
                elif len(mis_match) == 2:
                    if strs[i][mis_match[0]] == strs[j][mis_match[1]] and strs[j][mis_match[0]] == strs[i][mis_match[1]]: 
                        obj.union(i, j)
        
        result = 0
        for i in range(len(strs)):
            if obj.parent[i] == i:
                result += 1
        
        return result
                    
                
            
        