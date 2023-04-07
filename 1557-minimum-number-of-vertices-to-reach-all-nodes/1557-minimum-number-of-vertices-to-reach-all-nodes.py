class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        ans = set( i for i in range( n ))
        
        for edge in edges:
            
            if edge[1] in ans:
                ans.remove(edge[1])
        
        return ans