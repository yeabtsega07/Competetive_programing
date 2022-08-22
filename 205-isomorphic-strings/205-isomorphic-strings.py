class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
         return [s.find(i) for i in s] == [t.find(j) for j in t]
                
                    
                    
        