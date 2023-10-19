class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        class UnionFind:
            def __init__(self, n ):
                self.parent = [i for i in range(n)]
                # self.size = [1 for i in range(n)]
            
            def find(self, index):
                
                if self.parent[index] == index:
                    return index
                
                self.parent[index] = self.find(self.parent[index])
                return self.parent[index]
            
            def union(self, index1, index2):
                
                parent1, parent2 = self.find(index1), self.find(index2)
                
                if parent1 == parent2:
                    return

                    
                self.parent[parent2] = parent1

                
                return
        
        obj = UnionFind(n)
        obj.union(0, firstPerson)
        time_table = defaultdict(list)
        times = []
        for meeting in meetings:
            times.append(meeting[-1])
            time_table[meeting[-1]].append([meeting[0], meeting[1]])
            
        times = list(set(times))
        times.sort()                
           
        for time in times:
            cur = time_table[time]
            for val in cur:
                obj.union(val[0], val[1])
                
            req = obj.find(0)
            for val in cur:
                if obj.find(val[0]) != req:
                    obj.parent[val[0]] = val[0]
                    obj.parent[val[1]] = val[1]
            
            
        
        result, req = [], obj.find(0)
        for i in range(n):
            if obj.find(i) == req:
                result.append(i)
        
        return result
                            
            
        
        