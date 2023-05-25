class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        track = defaultdict(int)
        for bill in bills:
            
            if bill == 5:
                track[5] += 1
            elif bill == 10:
                if track[5]:
                    track[5] -= 1
                    track[10] += 1
                else:
                    return False
            else:
                cur = 15
                if track[10]:
                    cur -= 10
                    track[10] -= 1
                k = cur // 5
                if track[5] >= k:
                    track[5] -= k
                else:
                    return False
        return True
    
                
        