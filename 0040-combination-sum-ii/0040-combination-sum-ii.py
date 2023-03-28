class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        track = []
        candidates.sort()
        
        def subsets ( index = 0, cur = [], curSum = 0 ):
            
            if curSum == target:
                    
                track.append( cur[:] )
                
                return
            
            for i in range( index , len(candidates) ):
                
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target - curSum:
                    break
            
                cur.append( candidates[i] )
                subsets( i + 1, cur, curSum + candidates[i] )
                cur.pop()
            

        
        subsets( )
        
        return track
        