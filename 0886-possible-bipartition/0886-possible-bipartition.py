class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        if not dislikes:
            return True
        
        graph = defaultdict(list)
        
        for likes in dislikes:
            
            graph[likes[0]].append(likes[1])
            graph[likes[1]].append(likes[0])
            
        colors = {}
        
        def dfs( node, color ):
            
            colors[node] = color
            
            for child in graph[node]:
                if child in colors:

                    if colors[child] == color:
                        return False
                else:

                    if not dfs( child, 1 - color ):
                        return False
                    
            return True
            
        for node in range(1, n + 1):
            if node not in colors:

                if not dfs(node, 1):
                    return False

        return True