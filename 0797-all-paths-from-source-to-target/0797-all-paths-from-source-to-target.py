class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        result = []
        
        def dfs ( node, cur ):
            
            if node == len(graph) - 1:
                result.append( cur[:] )
                return
            
            
            for child in graph[node]:
                
                cur.append(child)
                dfs( child, cur )
                cur.pop()
            
        dfs( 0, [0] )
        
        return result
        