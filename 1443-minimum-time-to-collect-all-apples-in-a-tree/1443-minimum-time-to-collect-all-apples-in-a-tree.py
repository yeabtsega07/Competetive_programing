class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        
        for edge in edges:
            
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
            
        # res = 0
        visited = set()
        def dfs ( node ):
            
            count = 0
            visited.add(node)

            for child in graph[node]:
                
                if child not in visited:
                    check = dfs(child)

                    if check:
                        count += check
            
            if ( hasApple[node] or count ) and node != 0 :
                
                count += 2
            
            # print( count, node )
            return count
        
        return dfs( 0 )
        
          