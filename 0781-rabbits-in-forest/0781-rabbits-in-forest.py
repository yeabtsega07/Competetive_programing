class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        track  = defaultdict(int)
        count = 0
        
        for ans in answers:
            
            if ans in track:
                track[ans] -= 1
                
                if not track[ans]:
                    track.pop(ans)
            else:
                if ans:
                    track[ans] = ans
                count += ans
                count += 1
        
        return count
            
        