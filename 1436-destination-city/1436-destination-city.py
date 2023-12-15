class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        outDegree = defaultdict(int)
        cities = set()
        
        for path in paths:
            
            outDegree[path[0]] += 1
            cities.add(path[0])
            cities.add(path[1])
        
        for city in cities:
            if not outDegree[city]:
                return city
        
        
        
        