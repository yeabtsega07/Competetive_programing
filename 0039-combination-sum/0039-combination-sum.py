class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        res = []
        
        def recur( cand, target, res, index, track):
            
            if index == len(cand):
                if target == 0:
                    res.append(track[:])
                return
            
            if cand[index] <= target:
                track.append(cand[index])
                recur( cand, target - cand[index], res, index, track)
                track.pop()
            
            recur( cand , target, res, index + 1, track)
        
        recur(candidates, target, res, 0, [])
        return res