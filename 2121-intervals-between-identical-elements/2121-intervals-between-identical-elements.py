class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        track = defaultdict(list)
        res = [0]* len(arr)
        
        for i, num in enumerate(arr):
            
            track[num].append(i)
        
        for l in track.values():
            pre = 0
            curSum = sum(l)
            size = len(l)
            
            for i, n in enumerate(l):
        
                res[n] = (i*n - pre) + ((curSum-pre-n) - ((size-i-1)*n)) 
                pre += n

        return res    
            
            
            
            