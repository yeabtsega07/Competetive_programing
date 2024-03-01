class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res =[]
        
        def backtrack(opened = 0, closed = 0, track = [] ):
            
            if opened >= n and closed >= n:
                if opened == closed:
                    res.append("".join(track))
                
                return
            
            if opened < n:
                track.append("(")
                backtrack(opened + 1, closed, track)
                track.pop()
            
            if closed < opened:
                track.append(")")
                backtrack(opened, closed + 1, track)
                track.pop()
            
        
        backtrack()
        
        return res
            
            
                    
                    
        