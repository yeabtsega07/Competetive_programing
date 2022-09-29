class Solution:
    def frequencySort(self, s: str) -> str:
        track={}
        ans=""
        for char in s:
            track[char]=track.get(char,0)+1
        for val in sorted(track.items(), key=lambda x:x[1] , reverse=True):
              ans+=val[0]*val[1]
        return ans    
        
        
            
                
        