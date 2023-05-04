class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        
        for i, val in enumerate(parent):
            
            if val != -1:

                graph[val].append(i)    
        

        path = 1
        def dfs ( node ):
            
            count = 1
            nonlocal path
            
            if node not in graph.keys():
                return count
            
            max1, max2 = 0, 0 
            for child in graph[node]:

                    
                check = dfs( child )
                
                if s[child] != s[node]:

                    if check >= max1:
                        max2 = max1
                        max1 = check
                    elif check > max2:
                        max2 = check
                
            path = max(path, count + max2 + max1)  
            
            return count + max1   
        
        dfs( 0 )
        return path

