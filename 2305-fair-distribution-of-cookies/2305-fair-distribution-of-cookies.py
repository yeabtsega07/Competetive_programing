class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        track = [0] * k
        self.ans = float("inf")
        
        
        def backtrack (index):

            
            if index >= len(cookies):
                self.ans = min(self.ans, max(track))
                return
            
            if max(track) >= self.ans:
                return
            
            for i in range(k):
                
                track[i] += cookies[index]
                
                if track[i] >= self.ans:
                    track[i] -= cookies[index]
                    continue
                    
                backtrack(index + 1)
                track[i] -= cookies[index]
        
        
        backtrack(0)
        return self.ans   
  
    

                
        