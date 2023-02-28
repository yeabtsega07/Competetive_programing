class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        track, left, res = defaultdict(int), 0 , 0
        
        for right, fruit in enumerate(fruits):
            
            track[fruit] += 1
            
            while left < right and  len(track) > 2:
                
                track[fruits[left]] -= 1
                
                if track[fruits[left]] == 0:
                    track.pop(fruits[left])
                
                left += 1
            
            res = max(right - left + 1, res)
        
        return res